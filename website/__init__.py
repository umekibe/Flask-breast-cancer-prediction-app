from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os,joblib
from joblib import load
from os import path
from flask_login import LoginManager
from sqlalchemy.sql import func

basedir = path.abspath(path.dirname(__file__))

db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='kibeisagenius'
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    db.init_app(app)

    


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
     
    return app

def create_database(app):
    if not path.exists ('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template ('base.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/prediction')
def predict():
    return render_template ('prediction.html')










