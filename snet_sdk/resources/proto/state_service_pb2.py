# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state_service.proto

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
  name='state_service.proto',
  package='escrow',
  syntax='proto3',
  serialized_pb=_b('\n\x13state_service.proto\x12\x06\x65scrow\"<\n\x13\x43hannelStateRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"d\n\x11\x43hannelStateReply\x12\x15\n\rcurrent_nonce\x18\x01 \x01(\x0c\x12\x1d\n\x15\x63urrent_signed_amount\x18\x02 \x01(\x0c\x12\x19\n\x11\x63urrent_signature\x18\x03 \x01(\x0c\x32i\n\x1aPaymentChannelStateService\x12K\n\x0fGetChannelState\x12\x1b.escrow.ChannelStateRequest\x1a\x19.escrow.ChannelStateReply\"\x00\x62\x06proto3')
)




_CHANNELSTATEREQUEST = _descriptor.Descriptor(
  name='ChannelStateRequest',
  full_name='escrow.ChannelStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='escrow.ChannelStateRequest.channel_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='escrow.ChannelStateRequest.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=31,
  serialized_end=91,
)


_CHANNELSTATEREPLY = _descriptor.Descriptor(
  name='ChannelStateReply',
  full_name='escrow.ChannelStateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_nonce', full_name='escrow.ChannelStateReply.current_nonce', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_signed_amount', full_name='escrow.ChannelStateReply.current_signed_amount', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_signature', full_name='escrow.ChannelStateReply.current_signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=93,
  serialized_end=193,
)

DESCRIPTOR.message_types_by_name['ChannelStateRequest'] = _CHANNELSTATEREQUEST
DESCRIPTOR.message_types_by_name['ChannelStateReply'] = _CHANNELSTATEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelStateRequest = _reflection.GeneratedProtocolMessageType('ChannelStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELSTATEREQUEST,
  __module__ = 'state_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.ChannelStateRequest)
  ))
_sym_db.RegisterMessage(ChannelStateRequest)

ChannelStateReply = _reflection.GeneratedProtocolMessageType('ChannelStateReply', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELSTATEREPLY,
  __module__ = 'state_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.ChannelStateReply)
  ))
_sym_db.RegisterMessage(ChannelStateReply)



_PAYMENTCHANNELSTATESERVICE = _descriptor.ServiceDescriptor(
  name='PaymentChannelStateService',
  full_name='escrow.PaymentChannelStateService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=195,
  serialized_end=300,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetChannelState',
    full_name='escrow.PaymentChannelStateService.GetChannelState',
    index=0,
    containing_service=None,
    input_type=_CHANNELSTATEREQUEST,
    output_type=_CHANNELSTATEREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYMENTCHANNELSTATESERVICE)

DESCRIPTOR.services_by_name['PaymentChannelStateService'] = _PAYMENTCHANNELSTATESERVICE

# @@protoc_insertion_point(module_scope)
