from flask import Flask,jsonify,make_response
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api,Resource



app =  Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = 

migrate = Migrate(app,db)



from app import models
from app import routes

