from flask import Flask, render_template, redirect, url_for, request
from werkzeug import secure_filename

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import values

import os

app = Flask(__name__)
app.config.from_pyfile('utils/config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from utils import models, db_handler
db.create_all()


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/newstory/', methods=['GET', 'POST'])
def newstory():
	if request.method=='POST':
		title = request.form['title']
		text = request.form['text']
		story_id = db_handler.newStory(title, text)
		return redirect('/continue/'+story_id+'/')
	return render_template('newstory.html')

@app.route('/continue/<id>/')
def continueStory(id):
	if id=='0':
		print("0")
		story = db_handler.getRandomStory()
		return redirect('/continue/'+story.story_id+'/')
	else:
		story = db_handler.getStoryByStoryID(id)
	return render_template('continue.html', story=story)


@app.route('/add/<id>/', methods=['POST'])
def addToStory(id):
	text = request.form['text']
	db_handler.newTweet(text, id)
	return redirect('/continue/'+id+'/')



