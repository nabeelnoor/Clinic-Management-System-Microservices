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
import staff_pb2
import staff_pb2_grpc
from pymongo import MongoClient




def mongo():
    global client
    cluster = "mongodb+srv://HAdmin:nabeel123@cluster0.ypgny.mongodb.net/HMSDB?retryWrites=true&w=majority"
    client = MongoClient(cluster)
    # print(client.list_database_names())
    db = client.myFirstDatabase
    # return client
   # print(db.list_collection_names())


class StaffManager(staff_pb2_grpc.StaffManagerServicer):
    # def AddDoctor(self, request, context):
    #     print(client.list_database_names())
    #     mydb = client["myFirstDatabase"]        
    #     mycol = mydb["doctors"]
    #     mydict = {"name": request.name, "BirthDate": request.BirthDate,"Gender":request.Gender,"Fees":request.Fees,"Qualification":request.Qualification,"Role":request.Role}
    #     x = mycol.insert_one(mydict)
    #     return staff_pb2.AddDocReply(message='Hello, %s!' % request.name)
    
    def AddDepart(self, request, context):
        print(client.list_database_names())
        mydb = client["myFirstDatabase"]        
        mycol = mydb["dept"]
        mydict = {"name": request.name}
        x = mycol.insert_one(mydict)
        return staff_pb2.AddDeptReply(message="Successful")
    
    def ListDoctor(self, request, context):
        array = []
        arr1 = []
        print(client.list_database_names())
        mydb = client["myFirstDatabase"]        
        mycol = mydb["Emp"]
        print(mycol)
        for x in mycol.find({}, {'_id': False,"Password":False}):
            print("\ndataType:",x)
            if(x["DeptID"]==request.deptId):
                array.append(x)

        #print(array)
        return staff_pb2.listDocReply(message=array)
    
    def ListDepart(self, request, context):
        array = []
        arr1 = []
        print(client.list_database_names())
        mydb = client["myFirstDatabase"]        
        mycol = mydb["dept"]
        print(mycol)
        for x in mycol.find({}, {'_id': False}):
            # print(x)
            array.append(x)
        #print(array)
        return staff_pb2.listDeptReply(message=array)


def serve():
    # client=mongo() pip install pymongo dnspython
    # print(client.list_database_names())
    mongo()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    staff_pb2_grpc.add_StaffManagerServicer_to_server(StaffManager(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
