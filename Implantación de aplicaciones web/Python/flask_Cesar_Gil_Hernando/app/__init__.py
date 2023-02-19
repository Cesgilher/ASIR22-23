from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
#from config import Config

app=Flask(__name__)

#cargar la configuracion

app.config.from_object('config.DevelopmentConfig')

db=SQLAlchemy(app)

from .views.auth import auth
from .views.web import web
app.register_blueprint(auth)
app.register_blueprint(web)


with app.app_context():

    db.create_all()

