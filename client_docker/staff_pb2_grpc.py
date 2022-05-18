# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import staff_pb2 as staff__pb2


class StaffManagerStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddDepart = channel.unary_unary(
                '/staff.StaffManager/AddDepart',
                request_serializer=staff__pb2.AddDept.SerializeToString,
                response_deserializer=staff__pb2.AddDeptReply.FromString,
                )
        self.ListDoctor = channel.unary_unary(
                '/staff.StaffManager/ListDoctor',
                request_serializer=staff__pb2.listDoc.SerializeToString,
                response_deserializer=staff__pb2.listDocReply.FromString,
                )
        self.ListDepart = channel.unary_unary(
                '/staff.StaffManager/ListDepart',
                request_serializer=staff__pb2.listDept.SerializeToString,
                response_deserializer=staff__pb2.listDeptReply.FromString,
                )


class StaffManagerServicer(object):
    """The greeting service definition.
    """

    def AddDepart(self, request, context):
        """manage staff
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDoctor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDepart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StaffManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddDepart': grpc.unary_unary_rpc_method_handler(
                    servicer.AddDepart,
                    request_deserializer=staff__pb2.AddDept.FromString,
                    response_serializer=staff__pb2.AddDeptReply.SerializeToString,
            ),
            'ListDoctor': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDoctor,
                    request_deserializer=staff__pb2.listDoc.FromString,
                    response_serializer=staff__pb2.listDocReply.SerializeToString,
            ),
            'ListDepart': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDepart,
                    request_deserializer=staff__pb2.listDept.FromString,
                    response_serializer=staff__pb2.listDeptReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'staff.StaffManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StaffManager(object):
    """The greeting service definition.
    """

    @staticmethod
    def AddDepart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/staff.StaffManager/AddDepart',
            staff__pb2.AddDept.SerializeToString,
            staff__pb2.AddDeptReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDoctor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/staff.StaffManager/ListDoctor',
            staff__pb2.listDoc.SerializeToString,
            staff__pb2.listDocReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDepart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/staff.StaffManager/ListDepart',
            staff__pb2.listDept.SerializeToString,
            staff__pb2.listDeptReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
