# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: branch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62ranch.proto\"U\n\x12\x62ranchEventRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12$\n\nevent_type\x18\x02 \x01(\x0e\x32\x10.event_type_enum\x12\r\n\x05money\x18\x03 \x01(\x01\"g\n\x13\x62ranchEventResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12$\n\nevent_type\x18\x02 \x01(\x0e\x32\x10.event_type_enum\x12\r\n\x05money\x18\x03 \x01(\x01\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x01*7\n\x0f\x65vent_type_enum\x12\x0b\n\x07\x44\x45POSIT\x10\x00\x12\x0c\n\x08WITHDRAW\x10\x01\x12\t\n\x05query\x10\x02\x32O\n\x11\x62ranchEventSender\x12:\n\x0bMsgDelivery\x12\x13.branchEventRequest\x1a\x14.branchEventResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'branch_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EVENT_TYPE_ENUM']._serialized_start=208
  _globals['_EVENT_TYPE_ENUM']._serialized_end=263
  _globals['_BRANCHEVENTREQUEST']._serialized_start=16
  _globals['_BRANCHEVENTREQUEST']._serialized_end=101
  _globals['_BRANCHEVENTRESPONSE']._serialized_start=103
  _globals['_BRANCHEVENTRESPONSE']._serialized_end=206
  _globals['_BRANCHEVENTSENDER']._serialized_start=265
  _globals['_BRANCHEVENTSENDER']._serialized_end=344
# @@protoc_insertion_point(module_scope)
