from flask_restful import Resource
from flask_jwt_extended import jwt_required,create_refresh_token,create_access_token
from .. import models,request,api_
import datetime
from werkzeug.security import generate_password_hash


class User_(Resource):
    @jwt_required()
    def get(self):
        data = [user.to_json_serializeable() for user in models.User.query.all() ]
        return data,200
    def post(self):
        username = request.form['username']
        password = request.form['password']
        
        try:
            q = models.User(username=username)
            q.setPassword(password)
            models.db.session.add(q)
            models.db.session.commit()
            return {'mgs':'success','status':True}
        except Exception as e:
            return {'msg':f'{e}','status':False}
        
        
    def put(self):
        args = request.args['username']
        try:
            q = models.User.query.filter_by(username=args).first()
            q.username = request.form.get('username')
            q.password = request.form.get('password')
            models.db.session.commit()
            return {'msg':'updated','status':True}
        except Exception as e:
            return {'msg':f'{e}','status':False}

    def delete(self):
        args = request.args['username']
        if args == 'all':
            models.db.session.query(models.User).delete()
            models.db.session.commit()
            return {'msg':'deleted all !'},200

        try:
            q = models.User.query.filter_by(username=args).first()
            models.db.session.delete(q)
            return {'msg':"deleted",'status':True}
        except Exception as e:
            return {'msg':f'{e}','status':False}


def singleObject(data):
    return {'id':data.id,
            'username':data.username,
            'password':data.password,
            }

class Login(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form['password']
        user = models.User.query.filter_by(username=username).first()
        if not user:
            return {'msg':'username anda tidak terdaftar !'},404
        if not user.checkPassword(password):
            return {'msg':'password anda salah !'},404
        data = user.to_json_serializeable()
        
        expires = datetime.timedelta(hours=1)
        expires_refresh = datetime.timedelta(days=7)
        access_token = create_access_token(data,fresh=True,expires_delta=expires)
        refresh_token = create_refresh_token(data,expires_delta=expires_refresh)
        return {'msg':'success login!','access_token':access_token,'refresh_token':refresh_token},200
    
    
api_.add_resource(User_,'/api/user')
api_.add_resource(Login,'/api/login')


