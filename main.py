from flask import Flask, url_for,request
import Data
import json


app = Flask ("SunnyAPI")

@app.route("/sunny")
def hello():
    return "Hello World!"

@app.route('/',methods=['GET'])
def getallweather():
    
    connDatabase=Data.dataintable('localhost','postgres','sunny','sunny')
    listTables=connDatabase.get()
    return listTables[0]


@app.route('/',methods=['DELETE'])
def delete():
    pass


