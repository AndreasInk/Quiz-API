# -*- coding: utf-8 -*-


#!pip install  -U transformers==3.0.0

#!python -m  nltk.downloader punkt

# !git clone https://github.com/patil-suraj/question_generation.git




#!pip install flask-ngrok

from flask import Flask, request, Response
import json
import nlp
import streamlit as st

#run_with_ngrok(app)   #starts ngrok when the app is run


def quizify():
  

  textin = st.text_input("Input Text")

  quiz = nlp(textin)

  status = {}
  status['quiz'] = quiz

  statusjson = json.dumps(status)

  resp = Response(statusjson, status=200, mimetype='application/json')

  st.text(resp)



quizify()