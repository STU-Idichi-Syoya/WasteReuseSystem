# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_migrate import Migrate 
from flask_bcrypt import Bcrypt
import os
# init SQLAlchemy so we can use it later in our models

db = SQLAlchemy()
app=None
bcrypt=Bcrypt()

def create_app():
    global app,db,bcrypt
    tpath=os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__,template_folder=os.path.join(tpath,'templates'),static_folder=os.path.join(tpath,'static'),static_url_path='/')
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .users import users_app
    app.register_blueprint(users_app)
    
    print('items')
    from .items import items_app
    app.register_blueprint(items_app)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app