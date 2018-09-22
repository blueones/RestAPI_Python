from flask import Flask, url_for,request
import Data
import json
import jsonpickle


app = Flask ("SunnyAPI")

@app.route("/sunny")
def hello():
    return "Hello World!"

@app.route('/weather',methods=['GET'])
def getallweather():
    
    connDatabase=Data.dataintable('localhost','postgres','sunny','sunny')
    dataInTable=connDatabase.get()
    jsonfiedtabledata=jsonpickle.encode(dataInTable)
    return jsonfiedtabledata

@app.route('/',methods=['GET'])
def getalltables():
    
    connDatabase=Data.dataintable('localhost','postgres','sunny','sunny')
    listTables=connDatabase.tables()
    jsonfiedtables=jsonpickle.encode(listTables)
    return jsonfiedtables

@app.route('/',methods=['DELETE'])
def delete():
    pass


