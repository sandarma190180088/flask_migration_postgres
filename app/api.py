from app import api,Resource,User,ma,request,db,make_response,jsonify

# create mapping object dari sqlalchemy
class UserSchema(ma.Schema):
    class Meta:
        fields = ("username","password","created_at","id")
user_schema = UserSchema()
users_schema = UserSchema(many=True)



class User_(Resource):
    def get(self):
        
        data = [user.to_json_serializeable() for user in User.query.all() ]
        
        return data,200
        
        
    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            q = User(username=username,password=password)
            db.session.add(q)
            db.session.commit()
            return {'mgs':'success','status':True}
        except Exception as e:
            return {'msg':f'{e}','status':False}
    def put(self):
        args = request.args['username']
        try:
            q = User.query.filter_by(username=args).first()
            q.username = request.form.get('username')
            q.password = request.form.get('password')
            db.session.commit()
            return {'msg':'updated','status':True}
        except Exception as e:
            return {'msg':f'{e}','status':False}

    def delete(self):
        args = request.args['username']
        try:
            q = User.query.filter_by(username=args).first()
            db.session.delete(q)
            return {'msg':"deleted",'status':True}
        except Exception as e:
            return {'msg':f'{e}','status':False}





api.add_resource(User_,'/api/user')


