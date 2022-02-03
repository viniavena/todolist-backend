from app.models import BaseModel
from ..extensions import db
import bcrypt


class User(BaseModel):
    __tablename__ = 'users'

    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique = True)

    password_hash = db.Column(db.LargeBinary(128), nullable = False)
    
    lists = db.relationship('List', cascade="all, delete-orphan", backref='user')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash)
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
