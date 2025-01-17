from dndserver.config import config
from dndserver.database import db
from dndserver.enums.classes import CharacterClass, Gender
from dndserver.models import BlockedUser, Character
from dndserver.persistent import sessions
from dndserver.protos import PacketCommand as pc
from dndserver.protos.Defines import Define_Common
from dndserver.protos.Character import SACCOUNT_NICKNAME, SBLOCK_CHARACTER, SCHARACTER_FRIEND_INFO, Friend_Location
from dndserver.protos.Common import (
    SC2S_BLOCK_CHARACTER_LIST_REQ,
    SC2S_BLOCK_CHARACTER_REQ,
    SC2S_UNBLOCK_CHARACTER_REQ,
    SS2C_BLOCK_CHARACTER_LIST_RES,
    SS2C_BLOCK_CHARACTER_RES,
    SS2C_UNBLOCK_CHARACTER_RES,
)
from dndserver.protos.Defines import Define_Message
from dndserver.protos.Friend import SC2S_FRIEND_FIND_REQ, SS2C_FRIEND_FIND_RES, SS2C_FRIEND_LIST_ALL_RES
from dndserver.utils import get_user
from dndserver.handlers.party import get_party


def list_friends(ctx, msg):
    # send the loop start
    ctx.reply(SS2C_FRIEND_LIST_ALL_RES(loopFlag=Define_Message.LoopFlag.BEGIN))

    res = SS2C_FRIEND_LIST_ALL_RES()
    res.loopFlag = Define_Message.LoopFlag.PROGRESS

    # counters for the lobby and the dungeon
    in_lobby = 0
    in_dungeon = 0

    # process every character that is online. The client side will not show the current user in the list. So no need
    # to filter it out
    for user in sessions.values():
        # make sure the user is logged in to the lobby
        if user.character is None:
            continue

        nickname = SACCOUNT_NICKNAME(
            originalNickName=user.character.nickname, streamingModeNickName=user.character.streaming_nickname
        )

        friend_info = SCHARACTER_FRIEND_INFO()
        friend_info.accountId = str(user.account.id)
        friend_info.nickName.CopyFrom(nickname)
        friend_info.characterClass = CharacterClass(user.character.character_class).value
        friend_info.characterId = str(user.character.id)
        friend_info.gender = Gender(user.character.gender).value
        friend_info.level = user.character.level

        # get information about the party of the user
        party = get_party(account_id=user.account.id)
        is_solo = len(party.players) <= 1
        location = (
            Friend_Location.Friend_Location_DUNGEON
            if user.state.location == Define_Common.MetaLocation.INGAME
            else Friend_Location.Friend_Location_LOBBY
        )

        friend_info.locationStatus = location

        # Set the member count and max member count (special case for solo, that should be 0 not 1)
        friend_info.PartyMemeberCount = len(party.players) if not is_solo else 0
        friend_info.PartyMaxMemeberCount = 3 if not is_solo else 0

        # update the players in the dungeon and lobby
        if location == Friend_Location.Friend_Location_DUNGEON:
            in_dungeon += 1
        else:
            in_lobby += 1

        # add the user information to the friend list
        res.friendInfoList.append(friend_info)

    # set the total amount of users. TODO: Not sure if this is the correct location to set it
    res.totalUserCount = len(res.friendInfoList)

    # send all the friend data
    ctx.reply(res)

    # send the loop end
    return SS2C_FRIEND_LIST_ALL_RES(
        loopFlag=Define_Message.LoopFlag.END, lobbyLocateCount=in_lobby, dungeonLocateCount=in_dungeon
    )


def find_user(ctx, msg):
    # message SC2S_FRIEND_FIND_REQ {
    #   .DC.Packet.SACCOUNT_NICKNAME nickName = 1;
    # }
    req = SC2S_FRIEND_FIND_REQ()
    req.ParseFromString(msg)

    res = SS2C_FRIEND_FIND_RES(result=pc.SUCCESS)

    if not req.nickName.originalNickName:
        return res

    # Makes it so users can't search for or invite themselves.
    if req.nickName.originalNickName == sessions[ctx.transport].character.nickname:
        return res

    _, session = get_user(nickname=req.nickName.originalNickName)
    if session:
        # get information about the account we are requesting
        party = get_party(account_id=sessions[ctx.transport].account.id)
        is_solo = len(party.players) <= 1
        location = (
            Friend_Location.Friend_Location_DUNGEON
            if session.state.location == Define_Common.MetaLocation.INGAME
            else Friend_Location.Friend_Location_LOBBY
        )

        # add the friend info
        friend = SCHARACTER_FRIEND_INFO(
            accountId=str(session.account.id),
            nickName=SACCOUNT_NICKNAME(
                originalNickName=session.character.nickname,
                streamingModeNickName=session.character.streaming_nickname,
            ),
            characterClass=CharacterClass(session.character.character_class).value,
            characterId=str(session.character.id),
            gender=Gender(session.character.gender).value,
            level=session.character.level,
            locationStatus=location,
            PartyMemeberCount=len(party.players) if not is_solo else 0,
            PartyMaxMemeberCount=3 if not is_solo else 0,
        )
        res.friendInfo.CopyFrom(friend)

    return res


def block_user(ctx, msg):
    """Occurs when a character blocks another character."""
    req = SC2S_BLOCK_CHARACTER_REQ()
    req.ParseFromString(msg)

    blocker = sessions[ctx.transport]
    blocked_char = db.query(Character).filter_by(id=req.targetCharacterId, account_id=req.targetAccountId).first()
    if not blocked_char:
        return SS2C_BLOCK_CHARACTER_RES(result=pc.FAIL_BLOCK_CHARACTER_NOT_FOUND)

    dupe = db.query(BlockedUser).filter_by(blocked_by=blocker.character.id, account_id=blocked_char.account_id).first()
    if dupe:
        return SS2C_BLOCK_CHARACTER_RES(result=pc.FAIL_BLOCK_CHARACTER_ALREADY)

    blocks = db.query(BlockedUser).filter_by(blocked_by=blocker.character.id).count()
    if blocks >= config.game.settings.max_blocked_characters:
        return SS2C_BLOCK_CHARACTER_RES(result=pc.FAIL_BLOCK_CHARACTER_LIMIT)

    user = BlockedUser(
        blocked_by=blocker.character.id,
        account_id=int(blocked_char.account_id),
        character_id=int(blocked_char.id),
        nickname=blocked_char.nickname,
        character_class=CharacterClass(blocked_char.character_class),
        gender=Gender(blocked_char.gender),
    )
    user.save()

    res = SS2C_BLOCK_CHARACTER_RES(
        result=pc.SUCCESS,
        targetCharacterInfo=SBLOCK_CHARACTER(
            accountId=str(blocked_char.account_id),
            characterId=str(blocked_char.id),
            nickName=SACCOUNT_NICKNAME(
                originalNickName=blocked_char.nickname,
                streamingModeNickName=blocked_char.streaming_nickname,
                karmaRating=blocked_char.karma_rating,
            ),
            characterClass=CharacterClass(blocked_char.character_class).value,
            gender=Gender(blocked_char.gender).value,
        ),
    )
    return res


def unblock_user(ctx, msg):
    """Occurs when a character unblocks another character."""
    # message SC2S_UNBLOCK_CHARACTER_REQ {
    #   string targetAccountId = 1;
    #   string targetCharacterId = 2;
    # }
    req = SC2S_UNBLOCK_CHARACTER_REQ()
    req.ParseFromString(msg)

    blocker = sessions[ctx.transport]
    blocked_char = db.query(Character).filter_by(id=req.targetCharacterId, account_id=req.targetAccountId).first()
    if not blocked_char:
        return SS2C_BLOCK_CHARACTER_RES(result=pc.FAIL_BLOCK_CHARACTER_NOT_FOUND)

    query = (
        db.query(BlockedUser)
        .filter_by(blocked_by=blocker.character.id, character_id=int(req.targetCharacterId))
        .first()
    )
    query.delete()

    return SS2C_UNBLOCK_CHARACTER_RES(result=pc.SUCCESS, targetCharacterId=req.targetCharacterId)


def get_blocked_users(ctx, msg):
    # message SC2S_BLOCK_CHARACTER_LIST_REQ {}
    req = SC2S_BLOCK_CHARACTER_LIST_REQ()
    req.ParseFromString(msg)
    # message SS2C_BLOCK_CHARACTER_LIST_RES {
    #   repeated .DC.Packet.SBLOCK_CHARACTER blockCharacters = 1;
    # }
    res = SS2C_BLOCK_CHARACTER_LIST_RES()

    query = db.query(BlockedUser).filter_by(account_id=sessions[ctx.transport].account.id).all()
    if not query:
        return res

    for block in query:
        # The block doesn't contain the streaming mode nickname or karma rating.
        # TODO: Are these even needed for this?
        char = db.query(Character).filter_by(id=block.character_id).first()
        res.blockCharacters.append(
            SBLOCK_CHARACTER(
                accountId=str(block.account_id),
                characterId=str(block.character_id),
                nickName=SACCOUNT_NICKNAME(
                    originalNickName=block.nickname,
                    streamingModeNickName=char.streaming_nickname,
                    karmaRating=char.karma_rating,
                ),
                characterClass=CharacterClass(block.character_class).value,
                gender=Gender(block.gender).value,
            )
        )
    return res
