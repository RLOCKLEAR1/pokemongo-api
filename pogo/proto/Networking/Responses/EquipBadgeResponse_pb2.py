# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/EquipBadgeResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Data.Player import EquippedBadge_pb2 as Data_dot_Player_dot_EquippedBadge__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/EquipBadgeResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n-Networking/Responses/EquipBadgeResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x1f\x44\x61ta/Player/EquippedBadge.proto\"\xe3\x01\n\x12\x45quipBadgeResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32:.POGOProtos.Networking.Responses.EquipBadgeResponse.Result\x12\x37\n\x08\x65quipped\x18\x02 \x01(\x0b\x32%.POGOProtos.Data.Player.EquippedBadge\"H\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x13\n\x0f\x43OOLDOWN_ACTIVE\x10\x02\x12\x11\n\rNOT_QUALIFIED\x10\x03\x62\x06proto3')
  ,
  dependencies=[Data_dot_Player_dot_EquippedBadge__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_EQUIPBADGERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.EquipBadgeResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COOLDOWN_ACTIVE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_QUALIFIED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=271,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_EQUIPBADGERESPONSE_RESULT)


_EQUIPBADGERESPONSE = _descriptor.Descriptor(
  name='EquipBadgeResponse',
  full_name='POGOProtos.Networking.Responses.EquipBadgeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.EquipBadgeResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipped', full_name='POGOProtos.Networking.Responses.EquipBadgeResponse.equipped', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EQUIPBADGERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=343,
)

_EQUIPBADGERESPONSE.fields_by_name['result'].enum_type = _EQUIPBADGERESPONSE_RESULT
_EQUIPBADGERESPONSE.fields_by_name['equipped'].message_type = Data_dot_Player_dot_EquippedBadge__pb2._EQUIPPEDBADGE
_EQUIPBADGERESPONSE_RESULT.containing_type = _EQUIPBADGERESPONSE
DESCRIPTOR.message_types_by_name['EquipBadgeResponse'] = _EQUIPBADGERESPONSE

EquipBadgeResponse = _reflection.GeneratedProtocolMessageType('EquipBadgeResponse', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPBADGERESPONSE,
  __module__ = 'Networking.Responses.EquipBadgeResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.EquipBadgeResponse)
  ))
_sym_db.RegisterMessage(EquipBadgeResponse)


# @@protoc_insertion_point(module_scope)
