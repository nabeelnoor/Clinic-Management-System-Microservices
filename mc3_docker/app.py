from __future__ import print_function

import json
from flask import Flask,jsonify,request,render_template
import os
from concurrent import futures
import logging
from pymongo import MongoClient # to make connection with mongoDB
app= Flask(__name__)

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



@app.route("/makeAppointment",methods=['Get'])
def handshake():
    return jsonify({'response':'Hello from mc3'})

@app.route("/makeAppointment",methods=['Post'])
def makeAppointment():
    reqBody=request.json
    _Date=reqBody["Date"]
    _EmpId=reqBody["EmpId"]
    _UserId=reqBody["UserId"]
    client = mongo()
    mydb = client["myFirstDatabase"]        
    mycol = mydb["appointment"]
    appoint = {"UserId":_UserId,"EmpId":_EmpId,"Date":_Date,"Status":'false'}
    x = mycol.insert_one(appoint)      #insert appointment of an user with empid
    return jsonify({'result':'Appointment booked successfully at'+_Date})
    # return json.dumps({'name': 'alice',
    #                    'email': 'alice@outlook.com'})

@app.route("/getAppointment",methods=['Get'])
def getAppointment():
    client = mongo()
    array = []
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["appointment"]
    print(mycol)
    for x in mycol.find({"Status":"false"}, {'_id': False}):
        array.append(x)  #returns list of all appointments
    return jsonify({'appointments':array})

@app.route("/completeAppointment",methods=['Post'])
def CompleteAppointment():
    reqBody=request.json
    _Date=reqBody["Date"]
    _EmpId=reqBody["EmpId"]
    _UserId=reqBody["UserId"]
    client = mongo()
    array = []
    mydb = client["myFirstDatabase"]        
    mycol = mydb["appointment"]
    myquery = { "UserId": _UserId,"EmpId":_EmpId,"Date":_Date }
    newvalues = { "$set": { "Status": "true" } }
    mycol.update_one(myquery, newvalues)
    return jsonify({'response':"Appointment Completed"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 50054))
    app.run(debug=True, host='0.0.0.0', port=port)