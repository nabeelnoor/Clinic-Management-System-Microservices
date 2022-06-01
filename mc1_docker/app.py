from __future__ import print_function

import json
from flask import Flask,jsonify,request,render_template
import os
from concurrent import futures
from email import message
from locale import currency
import logging
import hashlib
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

def isEmpPresent(email):
    client = mongo()
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["Emp"]
    dbResponse=mycol.find_one({"EmpID":email})
    print(dbResponse)
    if(dbResponse==None):
        return False
    else:
        return True

def DBstoreEmp(EmpData):
    client = mongo()
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["Emp"]
    if(isEmpPresent(EmpData.EmpId)==True):
        return False
    currRecord = {"EmpID":EmpData.EmpId,"Name":EmpData.Name,"BirthDate":EmpData.BirthDate,"Password":EmpData.Password,"Gender":EmpData.Gender,"Qualification":EmpData.Qualification,"DeptID":EmpData.DeptID,"Role":EmpData.Role,"Fees":EmpData.Fees}
    x = mycol.insert_one(currRecord)
    return True

def DBauthEmp(email,password):
    client = mongo()
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["Emp"]
    dbResponse=mycol.find_one({"EmpID":email})
    if(dbResponse==None):
        return False,None
    if(dbResponse["Password"]!=password):
        return False,None
    return True,dbResponse["Role"]

# -----------------------------------------------------------------------Databases functions
app= Flask(__name__)

@app.route('/')
def handShake():
    return jsonify({"response":"handshake from mc1"})

@app.route("/registerUser",methods=['Post'])
def registerUser():
    retmsg="Not Successful"
    reqBody=request.json
    _name=reqBody["Name"]
    _userId=reqBody["UserID"]
    _password=reqBody["Password"]
    _birthDate=reqBody["BirthDate"]
    _gender=reqBody["Gender"]
    currUser=TestUser(_name,_userId,_password,_birthDate,_gender)
    dbResponse=DBStoreUser(currUser)
    if(dbResponse==True):
        retmsg="Successful"
    return jsonify({"response":retmsg})

@app.route("/authenticateUser",methods=['Post'])
def AuthenticateUser():
    reqBody=request.json
    _userId=reqBody["UserId"]
    _password=reqBody["Password"]
    retMsg="Not Successful"
    generatedToken="Null"
    if(DBauthUser(_userId,_password)==True):
        retMsg="Successful"
        generatedToken=hashlib.sha256(_userId.encode("utf-8")).hexdigest()
        TokenDB[_userId]=SecretClass(generatedToken,"user")
    return jsonify({"response":retMsg,"secretKey":generatedToken})

@app.route("/registerEmploy",methods=['Post'])
def RegisterEmploy():
    retMsg="Not Successful"
    reqBody=request.json
    _empId=reqBody["EmpID"]
    _name=reqBody["Name"]
    _birthDate=reqBody["BirthDate"]
    _gender=reqBody["Gender"]
    _qualification=reqBody["Qualification"]
    _fees=reqBody["Fees"]
    _deptId=reqBody["DeptID"]
    _role=reqBody["role"]
    _password=reqBody["Password"]
    currEmp=TestEmploy(_empId,_name,_birthDate,_gender,_qualification,_fees,_deptId,_role,_password)
    if(DBstoreEmp(currEmp)==True):
        retMsg="Successful"
    return jsonify({"response":retMsg})

@app.route("/authenticateEmploy",methods=["Post"])
def AuthenticateEmploy():
    reqBody=request.json
    _empId=reqBody["EmpID"]
    _password=reqBody["Password"]
    retMsg="Not Successful"
    generatedToken="Null"
    flag,responseRole=DBauthEmp(_empId,_password)
    if(flag==True):
        retMsg="Successful"
        generatedToken=hashlib.sha256(_empId.encode("utf-8")).hexdigest()
        print("CurrentRole:",responseRole)
        TokenDB[_empId]=SecretClass(generatedToken,responseRole)
    return jsonify({"reponse":retMsg,"secretKey":generatedToken})
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)