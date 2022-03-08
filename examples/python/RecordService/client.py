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
import RecordService_pb2
import RecordService_pb2_grpc
from flask import Flask,jsonify,request



def run():

    with grpc.insecure_channel('localhost:50054') as channel: #for another grpc call
        stub = RecordService_pb2_grpc.RecordServiceStub(channel)
        response = stub.SayHelloAgain(RecordService_pb2.HelloRequest(name='you'))
    print("AuthService client received: " + response.message)

    with grpc.insecure_channel('localhost:50054') as channel: #for another grpc call
        stub = RecordService_pb2_grpc.RecordServiceStub(channel)
        response = stub.SayHelloAgain(RecordService_pb2.HelloRequest(name='you'))
    print("AuthService client received: " + response.message)
   
   

if __name__ == '__main__':
    logging.basicConfig()
    run()




#Wrap all Flask apis inside this to make communication with the client.