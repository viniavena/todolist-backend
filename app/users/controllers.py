from flask import request, abort, make_response, jsonify
from flask.views import MethodView
from marshmallow_sqlalchemy import ValidationError
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token

from .model import User
from .schema import UserSchema


class UserCurrent(MethodView):

    decorators = [jwt_required()]

    def get(self): # /user/
        id = get_jwt_identity()
        user = User.query.get_or_404(id)
        user_schema = UserSchema()

        return user_schema.dump(user), 200

class UserCreate(MethodView):
    
    def post(self): # /signup/
        data = request.json
        schema = UserSchema()
        try:
            user = schema.load(data)
        except ValidationError as err:
            abort(
                make_response(
                    err.messages, 400
                )
            )

        user.save()
        return schema.dump(user), 200

    
class TestHealth(MethodView):
    
    def get(self): # /ping
        return {"Connection":"Success"},200
