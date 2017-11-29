from sqlalchemy import or_
from random import randint
from main import app, db
from .models import *
from .values import *
import requests


def IDExists(id):
    query = Story.query.filter_by(story_id=id).first()
    return (query == None)


def createID(length=6):
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
    return story_id


def addTextToStory(id, text):
    story = Story.query.get(id)
    story.full_text += (' ' + text)
    db.session.commit()


def getAllStories():
    stories = Story.query.all()
    return stories


def getAllPublicStories():
    stories = Story.query.all()
    return stories


def getRandomStory():
    stories = getAllPublicStories()
    chosen_one = randint(0, len(stories) - 1)
    return stories[chosen_one]


def getStoryByID(id):
    story = Story.query.get(id)
    return story


def getStoryByStoryID(story_id):
    story = Story.query.filter_by(story_id=story_id).first()
    return story


def newTweet(text, story_id):
    tweet = Tweet(text, story_id)
    addTweetToStory(tweet)
    db.session.add(tweet)
    db.session.commit()


def addTweetToStory(tweet):
    story = Story.query.filter_by(story_id=tweet.parent_story_id).first()
    story.full_text += (' ' + tweet.text)
    db.session.commit()



def checkCaptcha(captcha):
    r = requests.post(captcha_url, data={
        'secret': captcha_secret,
        'response': captcha
    })
    print(r.json())
    if r.status_code==200:
        return bool(r.json()['success'])
    else:
        app.logger.info(r.status_code)
        return False
