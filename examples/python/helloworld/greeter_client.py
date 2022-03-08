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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import staff_pb2
import staff_pb2_grpc
from pymongo import MongoClient 


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = staff_pb2_grpc.StaffManagerStub(channel)
        response = stub.AddDoctor(staff_pb2.AddDoc(EmpID=1,name='zulfi',BirthDate='05-06-1990',Gender='M',Fees=5000,Qualification='MBBS',Role='D'))
    print("Staff client received: " + response.message)
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = staff_pb2_grpc.StaffManagerStub(channel)
        response = stub.AddDepart(staff_pb2.AddDept(DeptID=1,name='Heart'))
    print("Staff client received: " + response.message)
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = staff_pb2_grpc.StaffManagerStub(channel)
        response = stub.ListDoctor(staff_pb2.listDoc())
    print(response.message)
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = staff_pb2_grpc.StaffManagerStub(channel)
        response = stub.ListDepart(staff_pb2.listDept())
    print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
