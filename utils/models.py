from main import app, db

class Story(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	full_text = db.Column(db.Text)

	def __init__(self, full_text, title):
		self.full_text = full_text
		self.title = title

class Tweet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(140))

	def __init__(self, text):
		self.text = text