import random

from dndserver import database
from dndserver.protos import Account_pb2 as acc
from dndserver.protos import Lobby_pb2 as lb
from dndserver.protos import InGame_pb2 as ig
from dndserver.protos import _Character_pb2 as char
from dndserver.protos import Common_pb2 as cmn


def enter_lobby(req):
    """Communication that occurs when loading into the lobby from the
    character selection screen."""
    res = acc.SS2C_LOBBY_ENTER_RES()
    res.result = 1
    db = database.get()
    result = db["characters"].find_one(id=req.characterId)
    res.accountId = str(result["owner_id"])
    return res


def region_select(ctx, req):
    """Currently unused."""
    # req = lb.SC2S_LOBBY_REGION_SELECT_REQ()
    # req.ParseFromString(data[8:])
    res = lb.SS2C_LOBBY_REGION_SELECT_RES()
    res.result = 1
    res.region = req.region
    return res


def start(req):
    """Currently unused."""
    # req = lb.SC2S_CHARACTER_SELECT_ENTER_REQ()
    # req.ParseFromString(data[8:])
    
    nickname = char.SACCOUNT_NICKNAME()
    nickname.originalNickName = "Krofty"
    nickname.streamingModeNickName = f"Fighter#{random.randrange(1000000, 1700000)}"
   
    res = ig.SS2C_ENTER_GAME_SERVER_NOT()
    res.port = 7777
    res.ip = "127.0.0.1"
    res.sessionId = "sess-2234"
    res.accountId = "104"
    res.isReconnect = 0
    return res


def enter(req):
    res = ig.SC2S_GAME_ENTER_COMPLETE_NOT()
    res.isSuccess = 1
    return res

def auto_reg(req):
    """Communication that occurs when loading into the lobby from the
    character selection screen."""
    res = ig.SS2C_AUTO_MATCH_REG_RES()
    res.result = 1
    return res

def meta_req(ctx, req):
    res = cmn.SS2C_META_LOCATION_RES()
    res.location = req.location
    return res