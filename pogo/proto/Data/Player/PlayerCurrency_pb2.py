# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Data/Player/PlayerCurrency.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Data/Player/PlayerCurrency.proto',
  package='POGOProtos.Data.Player',
  syntax='proto3',
  serialized_pb=_b('\n Data/Player/PlayerCurrency.proto\x12\x16POGOProtos.Data.Player\"\x1e\n\x0ePlayerCurrency\x12\x0c\n\x04gems\x18\x01 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERCURRENCY = _descriptor.Descriptor(
  name='PlayerCurrency',
  full_name='POGOProtos.Data.Player.PlayerCurrency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gems', full_name='POGOProtos.Data.Player.PlayerCurrency.gems', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['PlayerCurrency'] = _PLAYERCURRENCY

PlayerCurrency = _reflection.GeneratedProtocolMessageType('PlayerCurrency', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERCURRENCY,
  __module__ = 'Data.Player.PlayerCurrency_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.PlayerCurrency)
  ))
_sym_db.RegisterMessage(PlayerCurrency)


# @@protoc_insertion_point(module_scope)
