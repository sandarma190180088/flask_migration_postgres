from app import db 
from datetime import datetime

class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow())

    def __repr__(self) -> str:
        return f'<username = {self.username}>'


