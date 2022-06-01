from __future__ import print_function
import json
from flask import Flask,jsonify,request,render_template
import os
from concurrent import futures
import logging
from pymongo import MongoClient

app= Flask(__name__)



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

    

@app.route("/addDept",methods=['Post'])
def AddDepart():
    reqBody=request.json
    _name=reqBody["name"]
    client=mongo()
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["dept"]
    mydict = {"name": _name}
    x = mycol.insert_one(mydict)
    return jsonify({"result":"successful"})

@app.route("/listDoctors",methods=['Post'])
def ListDoctor():
    reqBody=request.json
    _deptId=reqBody["deptId"]
    array = []
    arr1 = []
    client=mongo()
    # print(client.list_database_names())
    mydb = client["myFirstDatabase"]      
    mycol = mydb["Emp"]
    print(mycol)
    for x in mycol.find({}, {'_id': False,"Password":False}):
        print("\ndataType:",x)
        if(x["DeptID"]==_deptId):
            array.append(x)
    return jsonify({"Doctors":array})


@app.route("/listDepartments",methods=['Get'])
def listDepartments():
    array = []
    arr1 = []
    client=mongo()
    print(client.list_database_names())
    mydb = client["myFirstDatabase"]        
    mycol = mydb["dept"]
    print(mycol)
    for x in mycol.find({}, {'_id': False}):
        array.append(x)
    return jsonify({"departments:":array})



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
