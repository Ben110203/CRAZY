#coding=utf-8

import logging
import time

from flask import Flask,request , abort

app = Flask(__name__)



@app.route("/")
def callback():
    return '<form id=_aa >hihi<input type=text   size=100>name=textbox></form>'
#@app.route("/", methods=['POST'])
#def callback():
#    body = request.get_data(as_text=True)
#    return '<a> %s </a>'%(body)
#hi

if __name__ == "__main__":
    app.run()

