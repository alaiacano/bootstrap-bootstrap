# Bootstrap-Bootstrap

This is a quick and dirty framework for getting apps running using the tornado web framework and bootstrap front-end framework. I've got a couple of little apps that use this stack and got tired of writing it over and over.

The boilerplate features are:

* A pretty layout
* User registration, log in, log out, password reset
* Basic User model with email, password, registered_on fields.
* User info page

The technology stack is:

* Heroku for hosting (but you could host it anywhere)
* Tornado for the web framework
* Mongodb for persistence (via MongoLab)
* MongoEngine for the ORM
* Redis for cache (via Redis To Go)
* Bootstrap for front end framework

# Setup instructions

These are things you'll have to do whether you run locally or on heroku:

* Clone this repo: `git clone git@github.com:alaiacano/bootstrap-bootstrap.git`
* Change the `cookie_secret` value to somathing else (`app.py`, line 15).

There's an `environment` file that the app will open to check on the environment. If it contains the string 'heroku', it will try to configure the databases from their cloud providers. Otherwise, it assumes mongo and redis are running locally on their default ports.

## Local mode

We'll have to set up mongo and redis. They're available from any package manager. I'm on OSX and use homebrew:

    brew install mongo
    brew install redis

Then you'll need to have the right python libraries installed:

    pip install tornado
    pip install mongoengine
    pip install redis

That should do it. Now start up your `mongod` and `redis-server` processes:

    mongod &
    redis-server &

And run your app:

    cd bootstrap-bootstrap
    python app.py

## Heroku mode

Set up accounts with MongoLab and Redis To Go. Then run the following commands to set the configuration variables on heroku.

    heroku config:add MONGO_UN=<mongo username>
    heroku config:add MONGO_PW=<mongo password>
    heroku config:add MONGO_HOST=<mongo host>
    heroku config:add MONGO_PORT=<mongo port>
    heroku config:add MONGO_db=<mongo database name>

After that, just follow the standard instructions for [deploying an app on heroku](https://devcenter.heroku.com/articles/git)

# Help

Am I doing something funadmentally wrong here? Let me know!
