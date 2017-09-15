from sqlalchemy import or_
from main import app,db
from .models import *
from .values import *
from random import randint

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

def IDExists(id):
	query = Story.query.get(id)
	return (query==None)