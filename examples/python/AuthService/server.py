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
import hashlib
import grpc
import AuthService_pb2
import AuthService_pb2_grpc

from StaffManager_pb2_grpc import StaffManagementStub 
import StaffManager_pb2

# my global working space act as db
class TestUser:
    def __init__(self,name,email,password,birthDate,gender):
        self.name=name
        self.email=email
        self.password=password
        self.gender=gender
        self.birthDate=birthDate
UserDB={}  #global datbase to store user data.

class SecretClass:
    def __init__(self,token,role):
        self.token=token
        self.role=role
TokenDB={}  #to make token

# my global working space act as db
class AuthServiceClass(AuthService_pb2_grpc.AuthServiceServicer):

    def SayHello(self, request, context):
        with grpc.insecure_channel('localhost:50051') as channel: #for another grpc call
            stub = StaffManagementStub(channel)
            response = stub.addDoctorProfile(StaffManager_pb2.DoctorDetials(DoctorID="Doc0001",Password="abcd",Qualification="Qualified",DeptID=100,Fees=2,JobTitle="Senior Doctor"))
        print("Greeter client received: " + response.message)
        return AuthService_pb2.HelloReply(message='Hello, %s!' % response)

    def SayHelloAgain(self, request, context):
        return AuthService_pb2.HelloReply(message='Hello Again, %s!' % request.name) 

    def RegisterUser(self,request,context):
        retmsg="Not Successful"
        if(request.UserID not in UserDB):
            retmsg="Successful"
            UserDB[request.UserID]=TestUser(request.Name,request.UserID,request.Password,request.BirthDate,request.Gender)
        # for each in UserDB:
        #     print(each.name,each.email)
        print("\n---------------------\n")
        return AuthService_pb2.UserRegisterationResponse(response=retmsg)
    
    def AuthenticateUser(self, request, context):
        retMsg="Not Successful";
        generatedToken="Null"
        if(request.UserID in UserDB):
            generatedToken=hashlib.sha256(request.UserID.encode("utf-8")).hexdigest()
            TokenDB[request.UserID]=SecretClass(generatedToken,"user")
        return AuthService_pb2.UserAuthenticationResponse(response=retMsg,secretKey=generatedToken)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    AuthService_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceClass(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
