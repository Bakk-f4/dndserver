# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _Chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dndserver.protos import _Character_pb2 as __Character__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b_Chat.proto\x12\tDC.Packet\x1a\x10_Character.proto\"8\n\x1dSCHATDATA_PIECE_ITEM_PROPERTY\x12\x0b\n\x03pid\x18\x01 \x01(\t\x12\n\n\x02pv\x18\x02 \x01(\x05\"\x9c\x01\n\x14SCHATDATA_PIECE_ITEM\x12\x0b\n\x03uid\x18\x01 \x01(\x04\x12\x0b\n\x03iid\x18\x02 \x01(\t\x12\x34\n\x02pp\x18\x03 \x03(\x0b\x32(.DC.Packet.SCHATDATA_PIECE_ITEM_PROPERTY\x12\x34\n\x02sp\x18\x04 \x03(\x0b\x32(.DC.Packet.SCHATDATA_PIECE_ITEM_PROPERTY\"^\n\x0fSCHATDATA_PIECE\x12\x0f\n\x07\x63hatStr\x18\x01 \x01(\t\x12:\n\x11\x63hatDataPieceItem\x18\x02 \x01(\x0b\x32\x1f.DC.Packet.SCHATDATA_PIECE_ITEM\"\xac\x01\n\tSCHATDATA\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x02 \x01(\t\x12.\n\x08nickname\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x0f\n\x07partyId\x18\x04 \x01(\t\x12\x36\n\x12\x63hatDataPieceArray\x18\x05 \x03(\x0b\x32\x1a.DC.Packet.SCHATDATA_PIECE\"P\n\x10SPIECE_ITEM_BODY\x12\x0b\n\x03idx\x18\x01 \x01(\r\x12/\n\x06pieces\x18\x02 \x01(\x0b\x32\x1f.DC.Packet.SCHATDATA_PIECE_ITEM\"?\n\x11SPIECE_ITEM_ARRAY\x12*\n\x05links\x18\x01 \x03(\x0b\x32\x1b.DC.Packet.SPIECE_ITEM_BODYB\x1a\n\x10\x63om.packets.chatB\x04\x63hatP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_Chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.packets.chatB\004chatP\000'
  _globals['_SCHATDATA_PIECE_ITEM_PROPERTY']._serialized_start=44
  _globals['_SCHATDATA_PIECE_ITEM_PROPERTY']._serialized_end=100
  _globals['_SCHATDATA_PIECE_ITEM']._serialized_start=103
  _globals['_SCHATDATA_PIECE_ITEM']._serialized_end=259
  _globals['_SCHATDATA_PIECE']._serialized_start=261
  _globals['_SCHATDATA_PIECE']._serialized_end=355
  _globals['_SCHATDATA']._serialized_start=358
  _globals['_SCHATDATA']._serialized_end=530
  _globals['_SPIECE_ITEM_BODY']._serialized_start=532
  _globals['_SPIECE_ITEM_BODY']._serialized_end=612
  _globals['_SPIECE_ITEM_ARRAY']._serialized_start=614
  _globals['_SPIECE_ITEM_ARRAY']._serialized_end=677
# @@protoc_insertion_point(module_scope)
