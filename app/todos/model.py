from email.policy import default
from app.models import BaseModel
from ..extensions import db
import enum

class PriorityChoices(enum.Enum):
    high = 1
    medium = 2
    low = 3

    def __str__(self):
        return self.value

class ToDo(BaseModel):
    __tablename__ = 'todos'
    
    title = db.Column(db.String(64), nullable=False)
    
    description = db.Column(db.Text, default="")
    
    priority = db.Column(PriorityChoices, nullable = False)

    done = db.Column(db.Boolean, default = False)

    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
