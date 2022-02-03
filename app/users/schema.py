from marshmallow import validates, ValidationError

from ..extensions import ma
from .model import User
from ..lists.schema import ListSchema

def validate_password(password):
    if len(password) < 6:
        raise ValidationError('Invalid password: Minimum 6 characters')

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    
    name = ma.String(required = True)

    email = ma.Email(required = True)
    
    password = ma.String(load_only = True, required = True , validate = validate_password)
    
    lists = ma.Nested(ListSchema, many = True, dump_only = True)

    @validates('name')
    def validate_name(self, name):
        if name == '':
            raise ValidationError('Invalid Name')