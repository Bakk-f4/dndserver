# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Karma.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dndserver.protos import _Character_pb2 as __Character__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bKarma.proto\x12\tDC.Packet\x1a\x10_Character.proto\"\xd1\x01\n\x15SKARMA_CHARACTER_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x02 \x01(\t\x12.\n\x08nickName\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\r\x12\x0e\n\x06isVote\x18\x06 \x01(\r\x12\x13\n\x0bkarmaAction\x18\x07 \x01(\r\x12\x13\n\x0bkarmaStatus\x18\x08 \x01(\r\"k\n\x1dSKARMA_MOST_RECENT_MATCH_INFO\x12\x10\n\x08matchIdx\x18\x01 \x01(\r\x12\x38\n\x0e\x63haracterInfos\x18\x02 \x03(\x0b\x32 .DC.Packet.SKARMA_CHARACTER_INFO\"\x1c\n\x1aSC2S_KARMA_REPORT_LIST_REQ\"\xc7\x01\n\x1aSS2C_KARMA_REPORT_LIST_RES\x12<\n\nmatchInfos\x18\x01 \x03(\x0b\x32(.DC.Packet.SKARMA_MOST_RECENT_MATCH_INFO\x12\x1a\n\x12\x63urrentTicketCount\x18\x02 \x01(\r\x12\x1b\n\x13\x63ollectionStepCount\x18\x03 \x01(\r\x12\x1a\n\x12maxCollectionCount\x18\x04 \x01(\r\x12\x16\n\x0emaxTicketCount\x18\x05 \x01(\r\"h\n\x1cSC2S_KARMA_REPORT_ACTION_REQ\x12\x10\n\x08matchIdx\x18\x01 \x01(\r\x12\x11\n\taccountId\x18\x02 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x03 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\r\"\xec\x01\n\x1cSS2C_KARMA_REPORT_ACTION_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x10\n\x08matchIdx\x18\x02 \x01(\r\x12=\n\x13updateCharacterInfo\x18\x03 \x01(\x0b\x32 .DC.Packet.SKARMA_CHARACTER_INFO\x12\x1a\n\x12\x63urrentTicketCount\x18\x04 \x01(\r\x12\x1b\n\x13\x63ollectionStepCount\x18\x05 \x01(\r\x12\x1a\n\x12maxCollectionCount\x18\x06 \x01(\r\x12\x16\n\x0emaxTicketCount\x18\x07 \x01(\r\"a\n\x1cSS2C_KARMA_RATING_UPDATE_NOT\x12\x19\n\x11updateKarmaRating\x18\x01 \x01(\x05\x12\x11\n\taccountId\x18\x02 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x03 \x01(\tB\x1c\n\x11\x63om.packets.karmaB\x05karmaP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Karma_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.packets.karmaB\005karmaP\000'
  _globals['_SKARMA_CHARACTER_INFO']._serialized_start=45
  _globals['_SKARMA_CHARACTER_INFO']._serialized_end=254
  _globals['_SKARMA_MOST_RECENT_MATCH_INFO']._serialized_start=256
  _globals['_SKARMA_MOST_RECENT_MATCH_INFO']._serialized_end=363
  _globals['_SC2S_KARMA_REPORT_LIST_REQ']._serialized_start=365
  _globals['_SC2S_KARMA_REPORT_LIST_REQ']._serialized_end=393
  _globals['_SS2C_KARMA_REPORT_LIST_RES']._serialized_start=396
  _globals['_SS2C_KARMA_REPORT_LIST_RES']._serialized_end=595
  _globals['_SC2S_KARMA_REPORT_ACTION_REQ']._serialized_start=597
  _globals['_SC2S_KARMA_REPORT_ACTION_REQ']._serialized_end=701
  _globals['_SS2C_KARMA_REPORT_ACTION_RES']._serialized_start=704
  _globals['_SS2C_KARMA_REPORT_ACTION_RES']._serialized_end=940
  _globals['_SS2C_KARMA_RATING_UPDATE_NOT']._serialized_start=942
  _globals['_SS2C_KARMA_RATING_UPDATE_NOT']._serialized_end=1039
# @@protoc_insertion_point(module_scope)
