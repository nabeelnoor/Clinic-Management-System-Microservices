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
"""The Python implementation of the GRPC AuthService.AuthService client."""

from __future__ import print_function

import logging

import grpc
import AuthService_pb2
import AuthService_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # with grpc.insecure_channel('localhost:50052') as channel:
    #     stub = AuthService_pb2_grpc.AuthServiceStub(channel)
    #     response = stub.SayHello(AuthService_pb2.HelloRequest(name='you'))
    # print("AuthService client received: " + response.message)
    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.SayHelloAgain(AuthService_pb2.HelloRequest(name='you'))
    print("AuthService client received: " + response.message)

    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.RegisterUser(AuthService_pb2.UserRegisterCredential(UserID="nab@gmail.com",Name="Nabeel",BirthDate="12/2/1999",Password="123",Gender='Male'))
    print("AuthService client received: " + response.response)

    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.AuthenticateUser(AuthService_pb2.UserCredentialRequest(UserID="nab2@gmail.com",Password="123"))
    print("AuthService client received: " + response.response)
    print("SecretToken:"+response.secretKey)
    # with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
    #     stub = AuthService_pb2_grpc.AuthServiceStub(channel)
    #     response = stub.LotteryGenerator(AuthService_pb2.LotteryRequest(randomNumber=11))
    # print("AuthService client received: " + response.response)


if __name__ == '__main__':
    logging.basicConfig()
    run()



#Wrap all Flask apis inside this to make communication with the client.