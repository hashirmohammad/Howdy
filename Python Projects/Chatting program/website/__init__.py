from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask import Flask, render_template
from flask_socketio import SocketIO, send
#creating database
db=SQLAlchemy()
DB_NAME="database.db"

#Creating the website
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='kaiokenx10'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    from .models import User

    create_database(app)
 
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    socketio=SocketIO(app,cors_allowed_origins='*')

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    @socketio.on('message')
    def handle_message(message):
        print("Received message: "+message)
        if message != "User connected!":
            send(message, broadcast=True)

    return app
# Creating a new database for a new user
def create_database(app):
    if not path.exists('website/'+DB_NAME):
        db.create_all(app=app)
        print('Created Database!')