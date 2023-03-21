from flask import Flask,jsonify,make_response,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api,Resource
from flask_marshmallow import Marshmallow
from flask_hashids import HashidMixin,Hashids
from flask_jwt_extended import *


app =  Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api_ = Api(app=app) 
ma = Marshmallow(app)
jwt = JWTManager(app=app)
hashids = Hashids(app)
migrate = Migrate(app,db) 



from .models import *
from . import restapi
from .routes import *

