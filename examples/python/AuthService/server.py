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
from locale import currency
import logging
import hashlib
import grpc
import AuthService_pb2
import AuthService_pb2_grpc

from StaffManager_pb2_grpc import StaffManagementStub 
import StaffManager_pb2
from pymongo import MongoClient # to make connection with mongoDB

#Databases Schemas
class TestUser:
    def __init__(self,name,email,password,birthDate,gender):
        self.name=name
        self.email=email
        self.password=password
        self.gender=gender
        self.birthDate=birthDate
UserDB={}  #global datbase to store user data.

class TestEmploy:
    def __init__(self,EmpId,Name,BirthDate,Gender,Qualification,Fees,DeptID,Role,Password):
        self.EmpId=EmpId
        self.Name=Name
        self.BirthDate=BirthDate
        self.Gender=Gender
        self.Qualification=Qualification
        self.Fees=Fees
        self.DeptID=DeptID
        self.Role=Role
        self.Password=Password
EmpDB={}

class SecretClass:
    def __init__(self,token,role):
        self.token=token
        self.role=role
TokenDB={}  #to make token

# Schemas for DB end here

globalClient=None
def mongo():
    global globalClient #to use it as the global variable
    if(globalClient==None):
        cluster = "mongodb+srv://HAdmin:nabeel123@cluster0.ypgny.mongodb.net/HMSDB?retryWrites=true&w=majority"
        client = MongoClient(cluster)
        # print(client.list_database_names())
        db = client.myFirstDatabase
        globalClient=client
        return globalClient
    else:
        return globalClient
# my global working space act as db

# ---------------------------------------------------------------Databases functions
def isUserPresent(email):
    client = mongo()
    mydb = client["myFirstDatabase"]        
    mycol = mydb["Users"]
    dbResponse=mycol.find_one({"UserID":email})
    print(dbResponse)
    if(dbResponse==None):
        return False
    else:
        return True

def DBStoreUser(UserData):    
    client = mongo()
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["Users"]
    if(isUserPresent(UserData.email)==True):
        return False
    currRecord = {"UserID":UserData.email,"Name":UserData.name,"BirthDate":UserData.birthDate,"Password":UserData.password,"Gender":UserData.gender}
    x = mycol.insert_one(currRecord)
    return True

# ---------------------------------------------------------------Databases functions
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
        currUser=TestUser(request.Name,request.UserID,request.Password,request.BirthDate,request.Gender)
        dbResponse=DBStoreUser(currUser)
        if(dbResponse==True):
            retmsg="Successful"
        print("\n-----------Inside User Registeration----------\n")
        return AuthService_pb2.UserRegisterationResponse(response=retmsg)
    
    def AuthenticateUser(self, request, context):
        retMsg="Not Successful"
        generatedToken="Null"
        if(request.UserID in UserDB):
            retMsg="Successful"
            generatedToken=hashlib.sha256(request.UserID.encode("utf-8")).hexdigest()
            TokenDB[request.UserID]=SecretClass(generatedToken,"user")
        return AuthService_pb2.UserAuthenticationResponse(response=retMsg,secretKey=generatedToken)
    
    def RegisterEmploy(self,request,context):
        retMsg="Not Successful"
        if(request.EmpID not in EmpDB):
            retMsg="Successful"
            EmpDB[request.EmpID]=TestEmploy(request.EmpID,request.Name,request.BirthDate,request.Gender,request.Qualification,request.Fees,request.DeptID,request.role,request.Password)
        return AuthService_pb2.EmployRegisterationResponse(response=retMsg)
    
    def AuthenticateEmploy(self,request,context):
        retMsg="Not Successful"
        generatedToken="Null"
        if(request.EmpID in EmpDB):
            retMsg="Successful"
            generatedToken=hashlib.sha256(request.EmpID.encode("utf-8")).hexdigest()
            currentEmp=EmpDB[request.EmpID]
            print("CurrentRole:",currentEmp.Role)
            TokenDB[request.EmpID]=SecretClass(generatedToken,currentEmp.Role)
        return AuthService_pb2.EmployAuthenticationResponse(response=retMsg,secretKey=generatedToken)
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    AuthService_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceClass(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
