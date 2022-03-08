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
from flask import Flask,jsonify,request

app= Flask(__name__)
# --------------Sample api for post# --------------Sample api for post# --------------Sample api for post
@app.route("/samplePost",methods=['Post'])
def testRoute():
    reqBody=request.json
    print(reqBody)
    print(reqBody['userid'])
    print(reqBody['password'])
    return jsonify({'response':"Sample Response"})
# --------------Sample api for post# --------------Sample api for post# --------------Sample api for post

@app.route("/registerUser",methods=['Post'])
def registerUser():
    reqBody=request.json
    # print(sample) print(sample['UserID']) (sample['Password'])
    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.RegisterUser(AuthService_pb2.UserRegisterCredential(UserID=reqBody['UserID'],Name=reqBody['Name'],BirthDate=reqBody['BirthDate'],Password=reqBody['Password'],Gender=reqBody['Gender']))
    print("AuthService client received: " + response.response)
    return jsonify({'response':response.response})

@app.route("/authenticateUser",methods=['Post'])
def AuthenticateUser():
    reqBody=request.json
    # print(sample) print(sample['UserID']) (sample['Password'])
    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.AuthenticateUser(AuthService_pb2.UserCredentialRequest(UserID=reqBody["UserID"],Password=reqBody["Password"]))
    return jsonify({'response':response.response,'secretKey':response.secretKey})

@app.route("/registerEmp",methods=['Post'])
def registerEmp():
    reqBody=request.json
    # print(sample) print(sample['UserID']) (sample['Password'])
    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.RegisterEmploy(AuthService_pb2.EmployRegisterCredential(EmpID=reqBody["EmpID"],Name=reqBody["Name"],BirthDate=reqBody["BirthDate"],Password=reqBody["Password"],Gender=reqBody["Gender"],Qualification=reqBody["Qualification"],Fees=reqBody["Fees"],role=reqBody["role"],DeptID=reqBody["DeptID"]))
    print("AuthService client received: " + response.response)
    return jsonify({'response':response.response})

@app.route("/authenticateEmp",methods=['Post'])
def AuthenticateEmp():
    reqBody=request.json
    # print(sample) print(sample['UserID']) (sample['Password'])
    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.AuthenticateEmploy(AuthService_pb2.EmployCredentialRequest(EmpID=reqBody["EmpID"],Password=reqBody["Password"]))
    return jsonify({'response':response.response,'secretKey':response.secretKey})

def run():

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
        response = stub.AuthenticateUser(AuthService_pb2.UserCredentialRequest(UserID="nab@gmail.com",Password="123"))
    print("AuthService client received: " + response.response)
    print("SecretToken:"+response.secretKey)

    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.RegisterEmploy(AuthService_pb2.EmployRegisterCredential(EmpID="doctor@gmail.com",Name="Nabeel",BirthDate="12/2/1999",Password="123",Gender='Male',Qualification="PHD",Fees=100,role="Doctor",DeptID=1))
    print("AuthService client received: " + response.response)

    with grpc.insecure_channel('localhost:50052') as channel: #for another grpc call
        stub = AuthService_pb2_grpc.AuthServiceStub(channel)
        response = stub.AuthenticateEmploy(AuthService_pb2.EmployCredentialRequest(EmpID="doctor@gmail.com",Password="123"))
    print("AuthService client received: " + response.response)
    print("Secret Token:"+response.secretKey)
   

if __name__ == '__main__':
    logging.basicConfig()
    # run()
    app.run(debug=True)



#Wrap all Flask apis inside this to make communication with the client.