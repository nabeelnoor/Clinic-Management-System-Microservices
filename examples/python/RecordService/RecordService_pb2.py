# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RecordService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13RecordService.proto\x12\rRecordService\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\";\n\x0cMKAppRequest\x12\x0e\n\x06UserId\x18\x01 \x01(\t\x12\r\n\x05\x45mpId\x18\x02 \x01(\t\x12\x0c\n\x04\x44\x61te\x18\x04 \x01(\t\"E\n\rMKAppResponse\x12\x10\n\x08response\x18\x01 \x01(\t\x12\r\n\x05\x41ppID\x18\x02 \x01(\t\x12\x13\n\x0bTokenNumber\x18\x03 \x01(\x05\x32\xf0\x01\n\rRecordService\x12\x44\n\x08SayHello\x12\x1b.RecordService.HelloRequest\x1a\x19.RecordService.HelloReply\"\x00\x12I\n\rSayHelloAgain\x12\x1b.RecordService.HelloRequest\x1a\x19.RecordService.HelloReply\"\x00\x12N\n\x0fmakeAppointment\x12\x1b.RecordService.MKAppRequest\x1a\x1c.RecordService.MKAppResponse\"\x00\x42<\n\x1eio.grpc.examples.RecordServiceB\x12RecordServiceProtoP\x01\xa2\x02\x03HLWb\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLOREPLY = DESCRIPTOR.message_types_by_name['HelloReply']
_MKAPPREQUEST = DESCRIPTOR.message_types_by_name['MKAppRequest']
_MKAPPRESPONSE = DESCRIPTOR.message_types_by_name['MKAppResponse']
HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'RecordService_pb2'
  # @@protoc_insertion_point(class_scope:RecordService.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'RecordService_pb2'
  # @@protoc_insertion_point(class_scope:RecordService.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

MKAppRequest = _reflection.GeneratedProtocolMessageType('MKAppRequest', (_message.Message,), {
  'DESCRIPTOR' : _MKAPPREQUEST,
  '__module__' : 'RecordService_pb2'
  # @@protoc_insertion_point(class_scope:RecordService.MKAppRequest)
  })
_sym_db.RegisterMessage(MKAppRequest)

MKAppResponse = _reflection.GeneratedProtocolMessageType('MKAppResponse', (_message.Message,), {
  'DESCRIPTOR' : _MKAPPRESPONSE,
  '__module__' : 'RecordService_pb2'
  # @@protoc_insertion_point(class_scope:RecordService.MKAppResponse)
  })
_sym_db.RegisterMessage(MKAppResponse)

_RECORDSERVICE = DESCRIPTOR.services_by_name['RecordService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036io.grpc.examples.RecordServiceB\022RecordServiceProtoP\001\242\002\003HLW'
  _HELLOREQUEST._serialized_start=38
  _HELLOREQUEST._serialized_end=66
  _HELLOREPLY._serialized_start=68
  _HELLOREPLY._serialized_end=97
  _MKAPPREQUEST._serialized_start=99
  _MKAPPREQUEST._serialized_end=158
  _MKAPPRESPONSE._serialized_start=160
  _MKAPPRESPONSE._serialized_end=229
  _RECORDSERVICE._serialized_start=232
  _RECORDSERVICE._serialized_end=472
# @@protoc_insertion_point(module_scope)
