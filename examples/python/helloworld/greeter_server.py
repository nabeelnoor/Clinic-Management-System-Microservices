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
import StaffManager_pb2
import StaffManager_pb2_grpc
from StaffManager_pb2_grpc import StaffManagement

class StaffManagement(StaffManager_pb2_grpc.StaffManagement):

    def SayHelloAgain(self, request, context):
        return StaffManager_pb2.HelloReply(message='Hello Again, %s!' % request.name) 

    def LotteryGenerator(self, request, context):
        testVariable=""
        if(request.randomNumber<10):
            testVariable="Yes"
        else:
            testVariable="No"
        return StaffManager_pb2.LotteryResponse(response=testVariable)

    def addDoctorProfile(self,request,context):
        return StaffManager_pb2.StorageReponse(message="Working")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    StaffManager_pb2_grpc.add_StaffManagementServicer_to_server(StaffManagement(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
