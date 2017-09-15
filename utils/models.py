from main import app, db

class Story(db.Model):
	__tablename__='story'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	story_id = db.Column(db.Text)
	title = db.Column(db.Text)
	full_text = db.Column(db.Text)

	def __init__(self, title, text, story_id):
		self.title = title
		self.full_text = text
		self.story_id = story_id

class Tweet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(140))

	def __init__(self, text):
		self.text = text