from app import app,User,jsonify
from flask_jwt_extended import jwt_required ,get_current_user,get_jwt_identity

@app.route('/')
def home():
    return [user.to_json_serializeable() for user in User.query.all()],200

@app.route('/user/<hashid:user_id>')
def user(user_id:int):
    user = User.query.get(user_id)
    if user is None:
        return jsonify('User not found'), 400
    return user.to_json_serializeable(), 200
@app.route('/protected',methods=['GET'])
@jwt_required()
def protected():
    # current_user = get_current_user()
    identity = get_jwt_identity()
    return jsonify({'currentUser':None,'identity':identity})

