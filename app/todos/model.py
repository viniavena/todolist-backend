from email.policy import default
from app.models import BaseModel
from ..extensions import db
import enum

class PriorityChoices(enum.Enum):
    high = 1
    medium = 2
    low = 3

class IntEnum(db.TypeDecorator):
    impl = db.Integer

    def __init__(self, enumtype, *args, **kwargs):
        super(IntEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):
            return value
        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)


class ToDo(BaseModel):
    __tablename__ = 'todo'
    
    title = db.Column(db.String(64), nullable=False)
    
    description = db.Column(db.Text, default="")
    
    priority = db.Column(IntEnum(PriorityChoices), nullable = False)

    done = db.Column(db.Boolean, nullable = False)

