from db import *
from mongoengine import *
import datetime

if ENVIRONMENT == 'heroku':
    connect('default', host='mongodb://%s:%s@%s:%s/%s' % (
            mongo_un, mongo_pw, mongo_host, mongo_port, mongo_db
        ))
else:
    connect('default')

class User(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    now = datetime.datetime.now()
    registered_on = DateTimeField(required=True, default=now)
