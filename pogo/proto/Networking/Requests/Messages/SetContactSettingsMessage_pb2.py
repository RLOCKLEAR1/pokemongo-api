# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Requests/Messages/SetContactSettingsMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Data.Player import ContactSettings_pb2 as Data_dot_Player_dot_ContactSettings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Requests/Messages/SetContactSettingsMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n<Networking/Requests/Messages/SetContactSettingsMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\x1a!Data/Player/ContactSettings.proto\"^\n\x19SetContactSettingsMessage\x12\x41\n\x10\x63ontact_settings\x18\x01 \x01(\x0b\x32\'.POGOProtos.Data.Player.ContactSettingsb\x06proto3')
  ,
  dependencies=[Data_dot_Player_dot_ContactSettings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SETCONTACTSETTINGSMESSAGE = _descriptor.Descriptor(
  name='SetContactSettingsMessage',
  full_name='POGOProtos.Networking.Requests.Messages.SetContactSettingsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contact_settings', full_name='POGOProtos.Networking.Requests.Messages.SetContactSettingsMessage.contact_settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=140,
  serialized_end=234,
)

_SETCONTACTSETTINGSMESSAGE.fields_by_name['contact_settings'].message_type = Data_dot_Player_dot_ContactSettings__pb2._CONTACTSETTINGS
DESCRIPTOR.message_types_by_name['SetContactSettingsMessage'] = _SETCONTACTSETTINGSMESSAGE

SetContactSettingsMessage = _reflection.GeneratedProtocolMessageType('SetContactSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _SETCONTACTSETTINGSMESSAGE,
  __module__ = 'Networking.Requests.Messages.SetContactSettingsMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.SetContactSettingsMessage)
  ))
_sym_db.RegisterMessage(SetContactSettingsMessage)


# @@protoc_insertion_point(module_scope)
