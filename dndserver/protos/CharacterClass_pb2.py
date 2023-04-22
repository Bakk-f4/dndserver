# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CharacterClass.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dndserver.protos import _Item_pb2 as __Item__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x43haracterClass.proto\x12\tDC.Packet\x1a\x0b_Item.proto\"q\n\x11SCLASS_EQUIP_INFO\x12\r\n\x05index\x18\x01 \x01(\r\x12\x17\n\x0fisAvailableSlot\x18\x02 \x01(\r\x12\x15\n\rrequiredLevel\x18\x03 \x01(\r\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\x0f\n\x07\x65quipId\x18\x05 \x01(\t\"M\n\x10SCLASS_MOVE_INFO\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\x0e\n\x06moveId\x18\x03 \x01(\t\x12\x0c\n\x04move\x18\x04 \x01(\r\"\x1b\n\x19SC2S_CLASS_LEVEL_INFO_REQ\"p\n\x19SS2C_CLASS_LEVEL_INFO_RES\x12\r\n\x05level\x18\x01 \x01(\r\x12\x0b\n\x03\x65xp\x18\x02 \x01(\r\x12\x10\n\x08\x65xpBegin\x18\x03 \x01(\r\x12\x10\n\x08\x65xpLimit\x18\x04 \x01(\r\x12\x13\n\x0brewardPoint\x18\x05 \x01(\r\"\x1b\n\x19SC2S_CLASS_EQUIP_INFO_REQ\"I\n\x19SS2C_CLASS_EQUIP_INFO_RES\x12,\n\x06\x65quips\x18\x01 \x03(\x0b\x32\x1c.DC.Packet.SCLASS_EQUIP_INFO\"\x1a\n\x18SC2S_CLASS_PERK_LIST_REQ\";\n\x18SS2C_CLASS_PERK_LIST_RES\x12\x1f\n\x05perks\x18\x01 \x03(\x0b\x32\x10.DC.Packet.SPerk\"\x1b\n\x19SC2S_CLASS_SKILL_LIST_REQ\">\n\x19SS2C_CLASS_SKILL_LIST_RES\x12!\n\x06skills\x18\x01 \x03(\x0b\x32\x11.DC.Packet.SSkill\"3\n\x19SC2S_CLASS_SPELL_LIST_REQ\x12\x16\n\x0emaxSpellMemory\x18\x01 \x01(\r\">\n\x19SS2C_CLASS_SPELL_LIST_RES\x12!\n\x06spells\x18\x01 \x03(\x0b\x32\x11.DC.Packet.SSpell\"G\n\x1eSC2S_CLASS_SPELL_SLOT_MOVE_REQ\x12\x0f\n\x07spellId\x18\x01 \x01(\t\x12\x14\n\x0c\x64stSlotIndex\x18\x02 \x01(\x05\"[\n\x1eSS2C_CLASS_SPELL_SLOT_MOVE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12)\n\x0e\x65quipSpellList\x18\x02 \x03(\x0b\x32\x11.DC.Packet.SSpell\"Q\n$SC2S_CLASS_SPELL_SEQUENCE_CHANGE_REQ\x12\x0f\n\x07spellId\x18\x01 \x01(\t\x12\x18\n\x10\x64stSequenceIndex\x18\x02 \x01(\r\"a\n$SS2C_CLASS_SPELL_SEQUENCE_CHANGE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12)\n\x0e\x65quipSpellList\x18\x02 \x03(\x0b\x32\x11.DC.Packet.SSpell\"v\n\x18SC2S_CLASS_ITEM_MOVE_REQ\x12,\n\x07oldMove\x18\x01 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFO\x12,\n\x07newMove\x18\x02 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFO\"\x86\x01\n\x18SS2C_CLASS_ITEM_MOVE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12,\n\x07oldMove\x18\x02 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFO\x12,\n\x07newMove\x18\x03 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFOB.\n\x1a\x63om.packets.characterClassB\x0e\x63haracterClassP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CharacterClass_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.packets.characterClassB\016characterClassP\000'
  _globals['_SCLASS_EQUIP_INFO']._serialized_start=48
  _globals['_SCLASS_EQUIP_INFO']._serialized_end=161
  _globals['_SCLASS_MOVE_INFO']._serialized_start=163
  _globals['_SCLASS_MOVE_INFO']._serialized_end=240
  _globals['_SC2S_CLASS_LEVEL_INFO_REQ']._serialized_start=242
  _globals['_SC2S_CLASS_LEVEL_INFO_REQ']._serialized_end=269
  _globals['_SS2C_CLASS_LEVEL_INFO_RES']._serialized_start=271
  _globals['_SS2C_CLASS_LEVEL_INFO_RES']._serialized_end=383
  _globals['_SC2S_CLASS_EQUIP_INFO_REQ']._serialized_start=385
  _globals['_SC2S_CLASS_EQUIP_INFO_REQ']._serialized_end=412
  _globals['_SS2C_CLASS_EQUIP_INFO_RES']._serialized_start=414
  _globals['_SS2C_CLASS_EQUIP_INFO_RES']._serialized_end=487
  _globals['_SC2S_CLASS_PERK_LIST_REQ']._serialized_start=489
  _globals['_SC2S_CLASS_PERK_LIST_REQ']._serialized_end=515
  _globals['_SS2C_CLASS_PERK_LIST_RES']._serialized_start=517
  _globals['_SS2C_CLASS_PERK_LIST_RES']._serialized_end=576
  _globals['_SC2S_CLASS_SKILL_LIST_REQ']._serialized_start=578
  _globals['_SC2S_CLASS_SKILL_LIST_REQ']._serialized_end=605
  _globals['_SS2C_CLASS_SKILL_LIST_RES']._serialized_start=607
  _globals['_SS2C_CLASS_SKILL_LIST_RES']._serialized_end=669
  _globals['_SC2S_CLASS_SPELL_LIST_REQ']._serialized_start=671
  _globals['_SC2S_CLASS_SPELL_LIST_REQ']._serialized_end=722
  _globals['_SS2C_CLASS_SPELL_LIST_RES']._serialized_start=724
  _globals['_SS2C_CLASS_SPELL_LIST_RES']._serialized_end=786
  _globals['_SC2S_CLASS_SPELL_SLOT_MOVE_REQ']._serialized_start=788
  _globals['_SC2S_CLASS_SPELL_SLOT_MOVE_REQ']._serialized_end=859
  _globals['_SS2C_CLASS_SPELL_SLOT_MOVE_RES']._serialized_start=861
  _globals['_SS2C_CLASS_SPELL_SLOT_MOVE_RES']._serialized_end=952
  _globals['_SC2S_CLASS_SPELL_SEQUENCE_CHANGE_REQ']._serialized_start=954
  _globals['_SC2S_CLASS_SPELL_SEQUENCE_CHANGE_REQ']._serialized_end=1035
  _globals['_SS2C_CLASS_SPELL_SEQUENCE_CHANGE_RES']._serialized_start=1037
  _globals['_SS2C_CLASS_SPELL_SEQUENCE_CHANGE_RES']._serialized_end=1134
  _globals['_SC2S_CLASS_ITEM_MOVE_REQ']._serialized_start=1136
  _globals['_SC2S_CLASS_ITEM_MOVE_REQ']._serialized_end=1254
  _globals['_SS2C_CLASS_ITEM_MOVE_RES']._serialized_start=1257
  _globals['_SS2C_CLASS_ITEM_MOVE_RES']._serialized_end=1391
# @@protoc_insertion_point(module_scope)
