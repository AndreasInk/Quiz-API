# -*- coding: utf-8 -*-


#!pip install  -U transformers==3.0.0

#!python -m  nltk.downloader punkt

# !git clone https://github.com/patil-suraj/question_generation.git




#!pip install flask-ngrok

from flask import Flask, request, Response
import json
import nlp
import streamlit
app = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run

@app.route("/quizify", methods=['POST'])
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



@app.route("/")
def home():
    return "<h1>Running Flask on Google Colab!</h1>"

app.run()