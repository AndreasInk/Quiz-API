# -*- coding: utf-8 -*-


#!pip install  -U transformers==3.0.0

#!python -m  nltk.downloader punkt

# !git clone https://github.com/patil-suraj/question_generation.git




#!pip install flask-ngrok

from flask_ngrok import run_with_ngrok
from flask import Flask, request, Response
import json
import nlp

myApp = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run

@myApp.route("/quizify", methods=['POST'])
def quizify():
  res = request.get_json()
  print (res)

  textin = res['text']

  quiz = nlp(textin)

  status = {}
  status['request'] = res
  status['quiz'] = quiz

  statusjson = json.dumps(status)

  resp = Response(statusjson, status=200, mimetype='application/json')

  return resp



@myApp.route("/")
def home():
    return "<h1>Running Flask on Google Colab!</h1>"
  
myApp.run()