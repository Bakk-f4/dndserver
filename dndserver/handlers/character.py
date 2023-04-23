import random
import time

from dndserver import database
from dndserver.objects import items
from dndserver.protos import (Account_pb2 as acc, _Character_pb2 as char,
                              CharacterClass_pb2 as cc,
                              _Defins_pb2 as df, Lobby_pb2 as lb,
                              _PacketCommand_pb2 as pc, _Item_pb2 as item)


def list_characters(ctx, req):
    """Communication that occurs when the user loads from the login to the
    character selection screen. Return a list of characters depending on
    the page of characters the user is currently on."""
    res = acc.SS2C_ACCOUNT_CHARACTER_LIST_RES()
    req.pageIndex = res.pageIndex = 1

    db = database.get()
    results = list(db["characters"].find(owner_id=ctx.sessions[ctx.transport]["accountId"]))

    start_index = (req.pageIndex - 1) * 7
    end_index = start_index + 7

    for result in results[start_index:end_index]:
        nickname = char.SACCOUNT_NICKNAME()
        nickname.originalNickName = result["nickname"]
        nickname.streamingModeNickName = f"Fighter#{random.randrange(1000000, 1700000)}"

        character = acc.SLOGIN_CHARACTER_INFO()
        character.nickName.CopyFrom(nickname)
        character.characterId = str(result["id"])
        character.characterClass = result["character_class"]
        character.createAt = result["created_at"]
        character.gender = result["gender"]
        character.level = result["level"]
        character.lastloginDate = result["last_logged_at"]

        character.equipItemList.append(items.generate_torch())
        character.equipItemList.append(items.generate_roundshield())
        character.equipItemList.append(items.generate_lantern())
        character.equipItemList.append(items.generate_sword())
        character.equipItemList.append(items.generate_pants())
        character.equipItemList.append(items.generate_tunic())
        character.equipItemList.append(items.generate_bandage())
        character.equipItemList.append(items.generate_helm())
        res.characterList.append(character)

    res.totalCharacterCount = len(results)

    return res

def create_character(ctx, req):
    """Communication that occurs when the user attempts to create a new
    character. Does basic sanity checking like the retail game and then
    stores the created character in the database."""
    res = acc.SS2C_ACCOUNT_CHARACTER_CREATE_RES()

    if len(req.nickName) < df.Define_Character.MIN:
        res.result = pc.PacketResult.Value("FAIL_CHARACTER_NICKNAME_LENGTH_SHORTAGE")
        return res

    if len(req.nickName) > df.Define_Character.MAX:
        res.result = pc.PacketResult.Value("FAIL_CHARACTER_NICKNAME_LENGTH_OVER")
        return res

    db = database.get()

    dupe = db["characters"].find_one(nickname=req.nickName)
    if dupe:
        res.result = pc.PacketResult.Value("FAIL_DUPLICATE_NICKNAME")
        return res

    db["characters"].insert(dict(
        owner_id=ctx.sessions[ctx.transport]["accountId"],
        nickname=req.nickName,
        gender=req.gender,
        character_class=req.characterClass,
        created_at=int(time.time()),
        level=1,
        last_logged_at=int(time.time())
    ))
    db.commit()
    db.close()

    res.result = 1
    return res


def delete_character(ctx, req):
    """Communication that occurs when the user deletes a character. Has basic
    sanity checking to make sure users don't delete others characters."""
    res = acc.SS2C_ACCOUNT_CHARACTER_DELETE_RES()

    db = database.get()
    char = db["characters"].find_one(id=req.characterId)

    # Prevents characters from maliciously deleting others characters.
    if char["owner_id"] != ctx.sessions[ctx.transport]["accountId"]:
        res.result = pc.PacketResult.Value("FAIL_GENERAL")
        return res

    db["characters"].delete(id=req.characterId)
    db.commit()
    db.close()

    res.result = pc.PacketResult.Value("SUCCESS")
    return res


def character_info(ctx):
    """Communication that occurs when the user loads into the lobby/tavern.
    Sends the game the relevant character information to be rendered in-game."""
    res = lb.SS2C_LOBBY_CHARACTER_INFO_RES()
    res.result = 1

    db = database.get()
    result = db["characters"].find_one(owner_id=ctx.sessions[ctx.transport]["accountId"])

    nickname = char.SACCOUNT_NICKNAME()
    nickname.originalNickName = result["nickname"]
    nickname.streamingModeNickName = f"Fighter#{random.randrange(1000000, 1700000)}"

    char_info = char.SCHARACTER_INFO()
    char_info.accountId = "1"
    char_info.nickName.CopyFrom(nickname)
    char_info.characterClass = result["character_class"]
    char_info.characterId = str(result["id"])
    char_info.gender = result["gender"]
    char_info.level = result["level"]

    char_info.CharacterItemList.append(items.generate_helm())
    char_info.CharacterItemList.append(items.generate_torch())
    char_info.CharacterItemList.append(items.generate_lantern())
    char_info.CharacterItemList.append(items.generate_sword())
    char_info.CharacterItemList.append(items.generate_pants())
    char_info.CharacterItemList.append(items.generate_tunic())
    char_info.CharacterItemList.append(items.generate_bandage())

    res.characterDataBase.CopyFrom(char_info)
    return res


def character_equip(ctx):
    """Communication that occurs when the user loads into the lobby/tavern.
    Sends the game the relevant character information to be rendered in-game."""
    equip = cc.SCLASS_EQUIP_INFO(
    index=1,
    isAvailableSlot=1,
    requiredLevel=1,
    type=1,
    equipId="1")

    res = cc.SS2C_CLASS_EQUIP_INFO_RES(equips=[equip])
    return res


def character_level(ctx):
    """Communication that occurs when the user loads into the lobby/tavern.
    Sends the game the relevant character information to be rendered in-game."""

    res = cc.SS2C_CLASS_LEVEL_INFO_RES(
        level=5, exp=1500, expBegin=1000, expLimit=2000, rewardPoint=1500)
    return res

def character_perks(ctx):
    """Communication that occurs when the user loads into the lobby/tavern.
    Sends the game the relevant character information to be rendered in-game."""
    res = cc.SS2C_CLASS_PERK_LIST_RES()
    res.perks.append(items.generate_two_hander())
    return res

def character_skills(ctx):
    """Communication that occurs when the user loads into the lobby/tavern.
    Sends the game the relevant character information to be rendered in-game."""
    res = cc.SS2C_CLASS_SKILL_LIST_RES()
    res.skills.append(items.generate_reckless())
    res.skills.append(items.generate_adrenaline())
    
    return res

def move_object(ctx):
    """Communication that occurs when the user loads into the lobby/tavern.
    Sends the game the relevant character information to be rendered in-game."""
    res = cc.SS2C_CLASS_ITEM_MOVE_RES()
    res.result = 2
    res.oldMove.append(items.move_info())
    res.newMove.append(items.new_move_info())
    
    return res