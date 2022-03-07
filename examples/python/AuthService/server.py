# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import AuthService_pb2
import AuthService_pb2_grpc

from StaffManager_pb2_grpc import StaffManagementStub 
import StaffManager_pb2

class AuthServiceClass(AuthService_pb2_grpc.AuthServiceServicer):

    def SayHello(self, request, context):
        with grpc.insecure_channel('localhost:50051') as channel: #for another grpc call
            stub = StaffManagementStub(channel)
            response = stub.addDoctorProfile(StaffManager_pb2.DoctorDetials(DoctorID="Doc0001",Password="abcd",Qualification="Qualified",DeptID=100,Fees=2,JobTitle="Senior Doctor"))
        print("Greeter client received: " + response.message)
        return AuthService_pb2.HelloReply(message='Hello, %s!' % response)

    def SayHelloAgain(self, request, context):
        return AuthService_pb2.HelloReply(message='Hello Again, %s!' % request.name) 

    # def LotteryGenerator(self, request, context):
    #     testVariable=""
    #     if(request.randomNumber<10):
    #         testVariable="Yes"
    #     else:
    #         testVariable="No"
    #     return AuthService_pb2.LotteryResponse(response=testVariable)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    AuthService_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceClass(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
