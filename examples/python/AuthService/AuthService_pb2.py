# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AuthService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x41uthService.proto\x12\x0b\x41uthService\"k\n\x16UserRegisterCredential\x12\x0e\n\x06UserID\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x11\n\tBirthDate\x18\x03 \x01(\t\x12\x10\n\x08Password\x18\x04 \x01(\t\x12\x0e\n\x06Gender\x18\x05 \x01(\t\"-\n\x19UserRegisterationResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"9\n\x15UserCredentialRequest\x12\x0e\n\x06UserID\x18\x01 \x01(\t\x12\x10\n\x08Password\x18\x02 \x01(\t\"A\n\x1aUserAuthenticationResponse\x12\x10\n\x08response\x18\x01 \x01(\t\x12\x11\n\tsecretKey\x18\x02 \x01(\t\"\xaf\x01\n\x18\x45mployRegisterCredential\x12\r\n\x05\x45mpID\x18\x01 \x01(\t\x12\x15\n\rQualification\x18\x02 \x01(\t\x12\x0c\n\x04\x46\x65\x65s\x18\x03 \x01(\x05\x12\x0e\n\x06\x44\x65ptID\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x0c\n\x04Name\x18\x06 \x01(\t\x12\x11\n\tBirthDate\x18\x07 \x01(\t\x12\x0e\n\x06Gender\x18\x08 \x01(\t\x12\x10\n\x08Password\x18\t \x01(\t\"/\n\x1b\x45mployRegisterationResponse\x12\x10\n\x08response\x18\x01 \x01(\t\":\n\x17\x45mployCredentialRequest\x12\r\n\x05\x45mpID\x18\x01 \x01(\t\x12\x10\n\x08Password\x18\x02 \x01(\t\"C\n\x1c\x45mployAuthenticationResponse\x12\x10\n\x08response\x18\x01 \x01(\t\x12\x11\n\tsecretKey\x18\x02 \x01(\t\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"&\n\x0eLotteryRequest\x12\x14\n\x0crandomNumber\x18\x01 \x01(\x05\"#\n\x0fLotteryResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\xf7\x04\n\x0b\x41uthService\x12@\n\x08SayHello\x12\x19.AuthService.HelloRequest\x1a\x17.AuthService.HelloReply\"\x00\x12\x45\n\rSayHelloAgain\x12\x19.AuthService.HelloRequest\x1a\x17.AuthService.HelloReply\"\x00\x12O\n\x10LotteryGenerator\x12\x1b.AuthService.LotteryRequest\x1a\x1c.AuthService.LotteryResponse\"\x00\x12]\n\x0cRegisterUser\x12#.AuthService.UserRegisterCredential\x1a&.AuthService.UserRegisterationResponse\"\x00\x12\x61\n\x10\x41uthenticateUser\x12\".AuthService.UserCredentialRequest\x1a\'.AuthService.UserAuthenticationResponse\"\x00\x12\x63\n\x0eRegisterEmploy\x12%.AuthService.EmployRegisterCredential\x1a(.AuthService.EmployRegisterationResponse\"\x00\x12g\n\x12\x41uthenticateEmploy\x12$.AuthService.EmployCredentialRequest\x1a).AuthService.EmployAuthenticationResponse\"\x00\x42\x38\n\x1cio.grpc.examples.AuthServiceB\x10\x41uthServiceProtoP\x01\xa2\x02\x03HLWb\x06proto3')



_USERREGISTERCREDENTIAL = DESCRIPTOR.message_types_by_name['UserRegisterCredential']
_USERREGISTERATIONRESPONSE = DESCRIPTOR.message_types_by_name['UserRegisterationResponse']
_USERCREDENTIALREQUEST = DESCRIPTOR.message_types_by_name['UserCredentialRequest']
_USERAUTHENTICATIONRESPONSE = DESCRIPTOR.message_types_by_name['UserAuthenticationResponse']
_EMPLOYREGISTERCREDENTIAL = DESCRIPTOR.message_types_by_name['EmployRegisterCredential']
_EMPLOYREGISTERATIONRESPONSE = DESCRIPTOR.message_types_by_name['EmployRegisterationResponse']
_EMPLOYCREDENTIALREQUEST = DESCRIPTOR.message_types_by_name['EmployCredentialRequest']
_EMPLOYAUTHENTICATIONRESPONSE = DESCRIPTOR.message_types_by_name['EmployAuthenticationResponse']
_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLOREPLY = DESCRIPTOR.message_types_by_name['HelloReply']
_LOTTERYREQUEST = DESCRIPTOR.message_types_by_name['LotteryRequest']
_LOTTERYRESPONSE = DESCRIPTOR.message_types_by_name['LotteryResponse']
UserRegisterCredential = _reflection.GeneratedProtocolMessageType('UserRegisterCredential', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERCREDENTIAL,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.UserRegisterCredential)
  })
_sym_db.RegisterMessage(UserRegisterCredential)

UserRegisterationResponse = _reflection.GeneratedProtocolMessageType('UserRegisterationResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERATIONRESPONSE,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.UserRegisterationResponse)
  })
_sym_db.RegisterMessage(UserRegisterationResponse)

UserCredentialRequest = _reflection.GeneratedProtocolMessageType('UserCredentialRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCREDENTIALREQUEST,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.UserCredentialRequest)
  })
_sym_db.RegisterMessage(UserCredentialRequest)

UserAuthenticationResponse = _reflection.GeneratedProtocolMessageType('UserAuthenticationResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAUTHENTICATIONRESPONSE,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.UserAuthenticationResponse)
  })
_sym_db.RegisterMessage(UserAuthenticationResponse)

EmployRegisterCredential = _reflection.GeneratedProtocolMessageType('EmployRegisterCredential', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYREGISTERCREDENTIAL,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.EmployRegisterCredential)
  })
_sym_db.RegisterMessage(EmployRegisterCredential)

EmployRegisterationResponse = _reflection.GeneratedProtocolMessageType('EmployRegisterationResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYREGISTERATIONRESPONSE,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.EmployRegisterationResponse)
  })
_sym_db.RegisterMessage(EmployRegisterationResponse)

EmployCredentialRequest = _reflection.GeneratedProtocolMessageType('EmployCredentialRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYCREDENTIALREQUEST,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.EmployCredentialRequest)
  })
_sym_db.RegisterMessage(EmployCredentialRequest)

EmployAuthenticationResponse = _reflection.GeneratedProtocolMessageType('EmployAuthenticationResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYAUTHENTICATIONRESPONSE,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.EmployAuthenticationResponse)
  })
_sym_db.RegisterMessage(EmployAuthenticationResponse)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

LotteryRequest = _reflection.GeneratedProtocolMessageType('LotteryRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOTTERYREQUEST,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.LotteryRequest)
  })
_sym_db.RegisterMessage(LotteryRequest)

LotteryResponse = _reflection.GeneratedProtocolMessageType('LotteryResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOTTERYRESPONSE,
  '__module__' : 'AuthService_pb2'
  # @@protoc_insertion_point(class_scope:AuthService.LotteryResponse)
  })
_sym_db.RegisterMessage(LotteryResponse)

_AUTHSERVICE = DESCRIPTOR.services_by_name['AuthService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034io.grpc.examples.AuthServiceB\020AuthServiceProtoP\001\242\002\003HLW'
  _USERREGISTERCREDENTIAL._serialized_start=34
  _USERREGISTERCREDENTIAL._serialized_end=141
  _USERREGISTERATIONRESPONSE._serialized_start=143
  _USERREGISTERATIONRESPONSE._serialized_end=188
  _USERCREDENTIALREQUEST._serialized_start=190
  _USERCREDENTIALREQUEST._serialized_end=247
  _USERAUTHENTICATIONRESPONSE._serialized_start=249
  _USERAUTHENTICATIONRESPONSE._serialized_end=314
  _EMPLOYREGISTERCREDENTIAL._serialized_start=317
  _EMPLOYREGISTERCREDENTIAL._serialized_end=492
  _EMPLOYREGISTERATIONRESPONSE._serialized_start=494
  _EMPLOYREGISTERATIONRESPONSE._serialized_end=541
  _EMPLOYCREDENTIALREQUEST._serialized_start=543
  _EMPLOYCREDENTIALREQUEST._serialized_end=601
  _EMPLOYAUTHENTICATIONRESPONSE._serialized_start=603
  _EMPLOYAUTHENTICATIONRESPONSE._serialized_end=670
  _HELLOREQUEST._serialized_start=672
  _HELLOREQUEST._serialized_end=700
  _HELLOREPLY._serialized_start=702
  _HELLOREPLY._serialized_end=731
  _LOTTERYREQUEST._serialized_start=733
  _LOTTERYREQUEST._serialized_end=771
  _LOTTERYRESPONSE._serialized_start=773
  _LOTTERYRESPONSE._serialized_end=808
  _AUTHSERVICE._serialized_start=811
  _AUTHSERVICE._serialized_end=1442
# @@protoc_insertion_point(module_scope)
