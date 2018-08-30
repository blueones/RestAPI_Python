from flask import Flask, url_for,request
from Data import *


app = Flask ("SunnyAPI")

@app.route("/sunny")
def hello():
    return "Hello World!"

@app.route('/',methods=['GET'])
def getallweather():



@app.route('/',methods=['DELETE'])
def delete():


