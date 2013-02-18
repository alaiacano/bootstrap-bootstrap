import redis
import os
from mongoengine import *

try:
    ENVIRONMENT = open('environment', 'r').read().strip()
except IOError:
    ENVIRONMENT = 'local'

if ENVIRONMENT == 'heroku':

    # setup up "redis to go"
    redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
    R = redis.from_url(redis_url)

    # get the mongo credentials. this must fail if the environment variables
    # aren't set.
    # Set environment variables with:
    # $ heroku config:add MONGO_UN=<mongo username>
    # $ heroku config:add MONGO_PW=<mongo password>
    # $ heroku config:add MONGO_HOST=<mongo host>
    # $ heroku config:add MONGO_PORT=<mongo port>
    # $ heroku config:add MONGO_db=<mongo database name>

    mongo_un = os.environ['MONGO_UN']
    mongo_pw = os.environ['MONGO_PW']
    mongo_db = os.environ['MONGO_DB']
    mongo_host = os.environ['MONGO_HOST']
    mongo_port = int(os.environ['MONGO_PORT'])

    connect('default', host='mongodb://%s:%s@%s:%s/%s' % (
        mongo_un, mongo_pw, mongo_host, mongo_port, mongo_db
    ))
else:
    # Local
    R = redis.StrictRedis()
    connect('default')
