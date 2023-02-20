from app import app,User,jsonify

@app.route('/')
def home():
    return [user.to_json_serializeable() for user in User.query.all()],200

@app.route('/user/<hashid:user_id>')
def user(user_id:int):
    user = User.query.get(user_id)
    if user is None:
        return jsonify('User not found'), 400
    return user.to_json_serializeable(), 200