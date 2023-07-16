from flask import Flask, render_template
import os
import openai
from classes.private import api_key
# from classes.Classe import Airtable

# at = Airtable()

# FUNCTIONS


# APP
app = Flask(__name__)


# Inici de la APP
@app.route('/',methods=['GET'])
def index(): # Home page

    openai.api_key = api_key

    response = openai.Completion.create(
        model="curie-similarity-fast",
        prompt="Create a list of 8 questions for my interview with a science fiction author:",
        temperature=0.5,
        max_tokens=10,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return render_template('index.html',response=response)