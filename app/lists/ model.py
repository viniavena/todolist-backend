from app.models import BaseModel
from ..extensions import db
import enum

class ToDo(BaseModel):
    __tablename__ = 'todo'
    
    title = db.Column(db.String(64), nullable=False)
    
    kind = db.Column(db.String(64), nullable=False)