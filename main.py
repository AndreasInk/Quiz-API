# -*- coding: utf-8 -*-


#!pip install  -U transformers==3.0.0

#!python -m  nltk.downloader punkt

# !git clone https://github.com/patil-suraj/question_generation.git




#!pip install flask-ngrok

from flask import Flask, request, Response
import json
from pipelines import pipeline
import streamlit as st
import nltk
import requests
#run_with_ngrok(app)   #starts ngrok when the app is run
nlp = pipeline("question-generation")
nltk.download('punkt')
def quizify():
  

  textin = st.text_input("")
  if textin != "":
    quiz = nlp(textin)

    status = {}
    status['quiz'] = quiz

    statusjson = json.dumps(status)

    resp = Response(statusjson, status=200, mimetype='application/json')

    st.text(quiz)
    return quiz



quizify()