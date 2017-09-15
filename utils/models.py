from main import app, db

class Story(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_text = db.Column(db.Text)

	def __init__(self, full_text):
		self.full_text = full_text

class Tweet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(140))

	def __init__(self, text):
		self.text = text