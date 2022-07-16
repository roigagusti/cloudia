from flask import Flask, render_template
from classes.Classe import Airtable

at = Airtable()

# FUNCTIONS


# APP
app = Flask(__name__)


# Inici de la APP
@app.route('/',methods=['GET'])
def index(): # Home page
    return render_template('index.html')