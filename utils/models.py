from main import app, db
from .values import *

class Story(db.Model):
	__tablename__='story'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	story_id = db.Column(db.Text)
	title = db.Column(db.Text)
	full_text = db.Column(db.Text)
	url = db.Column(db.Text)
	private = db.Column(db.Boolean, default=False)

	def __init__(self, title, text, story_id, private):
		self.title = title
		self.full_text = text
		self.story_id = story_id
		self.private = private
		self.url = app_url+'/continue/'+story_id+'/'

class Tweet(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	text = db.Column(db.String(140))
	parent_story_id = db.Column(db.Text)

	def __init__(self, text, parent):
		self.text = text
		self.parent_story_id = parent