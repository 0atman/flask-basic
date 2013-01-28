import os

from flask import Flask
from flask.ext import admin
from flask import render_template
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

from models import User, Todo, Tag, Post
from admin import UserView

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
app.config['MONGODB_SETTINGS'] = {'DB': 'testing'}

# Create models
connect(
    'flask-basic',
    host=os.environ.get(
        'MONGOLAB_URI',
        'mongodb://localhost/flask-basic'
    )
)
db = MongoEngine()
db.init_app(app)


# Flask views
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, 'Simple Models')

    # Add views
    admin.add_view(UserView(User))
    admin.add_view(ModelView(Todo))
    admin.add_view(ModelView(Tag))
    admin.add_view(ModelView(Post))

    # Start app
    app.debug = True
    app.run('0.0.0.0', 5000)
