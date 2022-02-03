from marshmallow import validates, ValidationError

from ..extensions import ma
from .model import ToDo

class ToDoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ToDo
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    
    title = ma.String(required = True)
    
    description = ma.String()
    
    priority = ma.String(required = True)

    done = ma.Boolean(required = True)