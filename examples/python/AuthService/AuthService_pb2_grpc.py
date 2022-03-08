# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import AuthService_pb2 as AuthService__pb2
import RecordService_pb2 as RecordService__pb2
import staff_pb2 as staff__pb2


class AuthServiceStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/AuthService.AuthService/SayHello',
                request_serializer=AuthService__pb2.HelloRequest.SerializeToString,
                response_deserializer=AuthService__pb2.HelloReply.FromString,
                )
        self.SayHelloAgain = channel.unary_unary(
                '/AuthService.AuthService/SayHelloAgain',
                request_serializer=AuthService__pb2.HelloRequest.SerializeToString,
                response_deserializer=AuthService__pb2.HelloReply.FromString,
                )
        self.LotteryGenerator = channel.unary_unary(
                '/AuthService.AuthService/LotteryGenerator',
                request_serializer=AuthService__pb2.LotteryRequest.SerializeToString,
                response_deserializer=AuthService__pb2.LotteryResponse.FromString,
                )
        self.RegisterUser = channel.unary_unary(
                '/AuthService.AuthService/RegisterUser',
                request_serializer=AuthService__pb2.UserRegisterCredential.SerializeToString,
                response_deserializer=AuthService__pb2.UserRegisterationResponse.FromString,
                )
        self.AuthenticateUser = channel.unary_unary(
                '/AuthService.AuthService/AuthenticateUser',
                request_serializer=AuthService__pb2.UserCredentialRequest.SerializeToString,
                response_deserializer=AuthService__pb2.UserAuthenticationResponse.FromString,
                )
        self.RegisterEmploy = channel.unary_unary(
                '/AuthService.AuthService/RegisterEmploy',
                request_serializer=AuthService__pb2.EmployRegisterCredential.SerializeToString,
                response_deserializer=AuthService__pb2.EmployRegisterationResponse.FromString,
                )
        self.AuthenticateEmploy = channel.unary_unary(
                '/AuthService.AuthService/AuthenticateEmploy',
                request_serializer=AuthService__pb2.EmployCredentialRequest.SerializeToString,
                response_deserializer=AuthService__pb2.EmployAuthenticationResponse.FromString,
                )
        self.ListOfAllDept = channel.unary_unary(
                '/AuthService.AuthService/ListOfAllDept',
                request_serializer=staff__pb2.listDept.SerializeToString,
                response_deserializer=staff__pb2.listDeptReply.FromString,
                )
        self.ListOfAllDoctor = channel.unary_unary(
                '/AuthService.AuthService/ListOfAllDoctor',
                request_serializer=staff__pb2.listDoc.SerializeToString,
                response_deserializer=staff__pb2.listDocReply.FromString,
                )
        self.AddDepartment = channel.unary_unary(
                '/AuthService.AuthService/AddDepartment',
                request_serializer=staff__pb2.AddDept.SerializeToString,
                response_deserializer=staff__pb2.AddDeptReply.FromString,
                )
        self.MakeAppointment3 = channel.unary_unary(
                '/AuthService.AuthService/MakeAppointment3',
                request_serializer=RecordService__pb2.MKAppRequest.SerializeToString,
                response_deserializer=RecordService__pb2.MKAppResponse.FromString,
                )
        self.CompleteAppointment3 = channel.unary_unary(
                '/AuthService.AuthService/CompleteAppointment3',
                request_serializer=RecordService__pb2.CompleteApp.SerializeToString,
                response_deserializer=RecordService__pb2.CompleteAppReply.FromString,
                )


class AuthServiceServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloAgain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LotteryGenerator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthenticateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterEmploy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthenticateEmploy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOfAllDept(self, request, context):
        """Calling to MC2
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOfAllDoctor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddDepartment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeAppointment3(self, request, context):
        """calling service from MC3
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteAppointment3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=AuthService__pb2.HelloRequest.FromString,
                    response_serializer=AuthService__pb2.HelloReply.SerializeToString,
            ),
            'SayHelloAgain': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHelloAgain,
                    request_deserializer=AuthService__pb2.HelloRequest.FromString,
                    response_serializer=AuthService__pb2.HelloReply.SerializeToString,
            ),
            'LotteryGenerator': grpc.unary_unary_rpc_method_handler(
                    servicer.LotteryGenerator,
                    request_deserializer=AuthService__pb2.LotteryRequest.FromString,
                    response_serializer=AuthService__pb2.LotteryResponse.SerializeToString,
            ),
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=AuthService__pb2.UserRegisterCredential.FromString,
                    response_serializer=AuthService__pb2.UserRegisterationResponse.SerializeToString,
            ),
            'AuthenticateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthenticateUser,
                    request_deserializer=AuthService__pb2.UserCredentialRequest.FromString,
                    response_serializer=AuthService__pb2.UserAuthenticationResponse.SerializeToString,
            ),
            'RegisterEmploy': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterEmploy,
                    request_deserializer=AuthService__pb2.EmployRegisterCredential.FromString,
                    response_serializer=AuthService__pb2.EmployRegisterationResponse.SerializeToString,
            ),
            'AuthenticateEmploy': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthenticateEmploy,
                    request_deserializer=AuthService__pb2.EmployCredentialRequest.FromString,
                    response_serializer=AuthService__pb2.EmployAuthenticationResponse.SerializeToString,
            ),
            'ListOfAllDept': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOfAllDept,
                    request_deserializer=staff__pb2.listDept.FromString,
                    response_serializer=staff__pb2.listDeptReply.SerializeToString,
            ),
            'ListOfAllDoctor': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOfAllDoctor,
                    request_deserializer=staff__pb2.listDoc.FromString,
                    response_serializer=staff__pb2.listDocReply.SerializeToString,
            ),
            'AddDepartment': grpc.unary_unary_rpc_method_handler(
                    servicer.AddDepartment,
                    request_deserializer=staff__pb2.AddDept.FromString,
                    response_serializer=staff__pb2.AddDeptReply.SerializeToString,
            ),
            'MakeAppointment3': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeAppointment3,
                    request_deserializer=RecordService__pb2.MKAppRequest.FromString,
                    response_serializer=RecordService__pb2.MKAppResponse.SerializeToString,
            ),
            'CompleteAppointment3': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteAppointment3,
                    request_deserializer=RecordService__pb2.CompleteApp.FromString,
                    response_serializer=RecordService__pb2.CompleteAppReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AuthService.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/SayHello',
            AuthService__pb2.HelloRequest.SerializeToString,
            AuthService__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloAgain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/SayHelloAgain',
            AuthService__pb2.HelloRequest.SerializeToString,
            AuthService__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LotteryGenerator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/LotteryGenerator',
            AuthService__pb2.LotteryRequest.SerializeToString,
            AuthService__pb2.LotteryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/RegisterUser',
            AuthService__pb2.UserRegisterCredential.SerializeToString,
            AuthService__pb2.UserRegisterationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthenticateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/AuthenticateUser',
            AuthService__pb2.UserCredentialRequest.SerializeToString,
            AuthService__pb2.UserAuthenticationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterEmploy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/RegisterEmploy',
            AuthService__pb2.EmployRegisterCredential.SerializeToString,
            AuthService__pb2.EmployRegisterationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthenticateEmploy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/AuthenticateEmploy',
            AuthService__pb2.EmployCredentialRequest.SerializeToString,
            AuthService__pb2.EmployAuthenticationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOfAllDept(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/ListOfAllDept',
            staff__pb2.listDept.SerializeToString,
            staff__pb2.listDeptReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOfAllDoctor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/ListOfAllDoctor',
            staff__pb2.listDoc.SerializeToString,
            staff__pb2.listDocReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddDepartment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/AddDepartment',
            staff__pb2.AddDept.SerializeToString,
            staff__pb2.AddDeptReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MakeAppointment3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/MakeAppointment3',
            RecordService__pb2.MKAppRequest.SerializeToString,
            RecordService__pb2.MKAppResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteAppointment3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService.AuthService/CompleteAppointment3',
            RecordService__pb2.CompleteApp.SerializeToString,
            RecordService__pb2.CompleteAppReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
