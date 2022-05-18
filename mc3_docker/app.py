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
# from email import message
# from locale import currency
import logging
# import hashlib
# from msilib.schema import AppId
# from urllib import response
import grpc
import RecordService_pb2
import RecordService_pb2_grpc

# from StaffManager_pb2_grpc import StaffManagementStub 
# import StaffManager_pb2
from pymongo import MongoClient # to make connection with mongoDB

#Databases Schemas
class Payment:
    def __init__(self,name,email,password,birthDate,gender):
        self.name=name
        self.email=email
        self.password=password
        self.gender=gender
        self.birthDate=birthDate


class Appointment:
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

class Prescription:
    def __init__(self,name):
        self.name=name

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

def DBauthUser(email,password):
    client = mongo()
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["Users"]
    dbResponse=mycol.find_one({"UserID":email})
    if(dbResponse==None):
        return False
    if(dbResponse["Password"]!=password):
        return False
    return True

def DBStoreApp():
    return True
    
# -----------------------------------------------------------------------Databases functions
class RecordServiceClass(RecordService_pb2_grpc.RecordServiceServicer):

    def SayHello(self, request, context):
        return RecordService_pb2.HelloReply(message='Hello')

    def SayHelloAgain(self, request, context):
        return RecordService_pb2.HelloReply(message='Hello Again, %s!' % request.name) 

    def makeAppointment(self, request, context):
        client = mongo()
        mydb = client["myFirstDatabase"]        
        mycol = mydb["appointment"]
        appoint = {"UserId":request.UserId,"EmpId":request.EmpId,"Date":request.Date,"Status":'false'}
        x = mycol.insert_one(appoint)      #insert appointment of an user with empid
        return RecordService_pb2.MKAppResponse(message="Appointment Booked Successfully at "+request.Date)
    
    def getAppointment(self, request, context):
        client = mongo()
        array = []
        print(client.list_database_names())
        mydb = client["myFirstDatabase"]        
        mycol = mydb["appointment"]
        print(mycol)
        for x in mycol.find({"Status":"false"}, {'_id': False}):
            # print(x)
            array.append(x)  #returns list of all appointments
        #print(array)
        return RecordService_pb2.getAppReply(message=array)
    
    def CompleteAppointment(self, request, context):
        client = mongo()
        array = []
        print(client.list_database_names())
        mydb = client["myFirstDatabase"]        
        mycol = mydb["appointment"]
        myquery = { "UserId": request.UserId,"EmpId":request.EmpId,"Date":request.Date }
        newvalues = { "$set": { "Status": "true" } }

        mycol.update_one(myquery, newvalues)
        return RecordService_pb2.CompleteAppReply(message="Appointment Completed")
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    RecordService_pb2_grpc.add_RecordServiceServicer_to_server(RecordServiceClass(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
