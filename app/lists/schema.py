from marshmallow import validates, ValidationError

from ..todos.schema import ToDoSchema
from ..extensions import ma
from .model import List

class ListSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = List
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    
    title = ma.String(required = True)
    
    kind = ma.String(required = True)

    todos = ma.Nested(ToDoSchema, many = True, dump_only = True)