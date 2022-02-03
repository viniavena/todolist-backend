from app.models import BaseModel
from ..extensions import db

class List(BaseModel):
    __tablename__ = 'lists'
    
    title = db.Column(db.String(64), nullable=False)
    
    kind = db.Column(db.String(64), nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    lists = db.relationship('List', cascade="all, delete-orphan", backref='list')