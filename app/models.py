from . import db,HashidMixin,hashids
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(HashidMixin,db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer,primary_key=True)
    
    username = db.Column(db.String(30),nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow())

    def __repr__(self) -> str:
        return f'<username = {self.username}>'
    def to_json_serializeable(self):
        return {"id":self.hashid,"name":self.username,"created_at":self.created_at.strftime("%A, %d %B %Y")}
    
    def setPassword(self,password):
        self.password = generate_password_hash(password)
    def checkPassword(self,password):
        return check_password_hash(self.password,password)




