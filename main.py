from flask import Flask, url_for,request
import Data
import json
import jsonpickle


app = Flask ("SunnyAPI")

@app.route("/sunny")
def hello():
    return "Hello World!"

@app.route('/',methods=['GET'])
def getallweather():
    
    connDatabase=Data.dataintable('localhost','postgres','sunny','sunny')
    listTables=connDatabase.get()
    jsonfiedtabledata=jsonpickle.encode(listTables)
    return jsonfiedtabledata


@app.route('/',methods=['DELETE'])
def delete():
    pass


