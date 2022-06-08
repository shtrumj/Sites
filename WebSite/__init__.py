from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '4i9vfiubninjrfiu39n jidh9w0kdk fkdinbi8orhe89jdf'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}'
    db.init_all(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Sites, Users, Servers

    create_database(app)
    return app


def create_database(app):
    if not path.exists('WebSite/' + DB_NAME):
        db.create_all(app=app)
        print('Database Was Created!')
