#-*- coding> utf-8 -*-
import csv
from flask import Flask, render_template, request
from services.votesService import votesService
import csv

from controllers.votesController import votesController


app = Flask(__name__)

@app.route('/')
def index():
   votes = votesService.get()
   return render_template('index.html', rick_votes=votes['Rick Sanchez'], jesus_votes=votes['Jesus Cristo'], darth_votes=votes['Darth Vader'], romer_votes=votes['Romer Simpson'], michael_votes=votes['Michael Jackson'])

@app.route('/votes', methods = ['GET', 'POST'])
def votes():
    return votesController.use(request)       

app.run(debug = True)