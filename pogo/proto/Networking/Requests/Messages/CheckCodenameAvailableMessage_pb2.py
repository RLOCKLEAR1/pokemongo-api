# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Requests/Messages/CheckCodenameAvailableMessage.proto

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
  name='Networking/Requests/Messages/CheckCodenameAvailableMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n@Networking/Requests/Messages/CheckCodenameAvailableMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"1\n\x1d\x43heckCodenameAvailableMessage\x12\x10\n\x08\x63odename\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKCODENAMEAVAILABLEMESSAGE = _descriptor.Descriptor(
  name='CheckCodenameAvailableMessage',
  full_name='POGOProtos.Networking.Requests.Messages.CheckCodenameAvailableMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codename', full_name='POGOProtos.Networking.Requests.Messages.CheckCodenameAvailableMessage.codename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=109,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['CheckCodenameAvailableMessage'] = _CHECKCODENAMEAVAILABLEMESSAGE

CheckCodenameAvailableMessage = _reflection.GeneratedProtocolMessageType('CheckCodenameAvailableMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHECKCODENAMEAVAILABLEMESSAGE,
  __module__ = 'Networking.Requests.Messages.CheckCodenameAvailableMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.CheckCodenameAvailableMessage)
  ))
_sym_db.RegisterMessage(CheckCodenameAvailableMessage)


# @@protoc_insertion_point(module_scope)
