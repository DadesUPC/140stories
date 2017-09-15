from sqlalchemy import or_
from random import randint
from main import app,db
from .models import *
from .values import *

def IDExists(id):
	query = Story.query.filter_by(story_id=id).first()
	return (query==None)


def createID(length = 6):
	ret = ""
	i = 0
	for i in range(length):
		n = randint(0, 35)
		if n > 25:
			n += 22
		else:
			n += 97
		ret = ret[:i] + str(chr(n)) + ret[i + 1:]
	return ret


def newStory(title, text):
	story_id = createID()
	story = Story(title, text, story_id)
	db.session.add(story)
	db.session.commit()

def addTextToStory(id, text):
	story = Story.query.get(id)
	story.full_text+=text
	db.session.commit()
