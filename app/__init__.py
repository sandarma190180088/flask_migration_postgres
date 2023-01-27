from flask import Flask,jsonify,make_response,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api,Resource
from flask_marshmallow import Marshmallow


app =  Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app=app) 
ma = Marshmallow(app)

migrate = Migrate(app,db) 



from app.models import User
from app.api import *
from app.routes import *

