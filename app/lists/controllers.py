from flask import request, abort, make_response
from flask.view import MethodView

from marshmallow import ValidationError

from flask_jwt_extended import jwt_required, get_jwt_identify

from .schema import ListSchema
from .model import List
from ..users.model import User

def validate_user_id(id):
    user = User.query.filter_by(id = id).first()
    if not user:
        abort(
            make_response(
                {"Error":"Token Identify Error"}, 401
            )
        )
    return user


class ListFunctions(MethodView):
    decorators = [jwt_required()]

    # /list/new
    def post(self):
        user_id = get_jwt_identify()
        validate_user_id (user_id)

        data = request.json
        schema = ListSchema()

        try: 
            list = schema.load(data)
        except ValidationError as err:
            abort(
                make_response(err.messages, 400)
            )
        
        list.save()
        
        return schema.dump(list), 200
    
    # list/<int:list_id>
    def get(self, list_id):
        user_id = get_jwt_identify()
        validate_user_id (user_id)

        list = List.query.get_or_404(list_id)

        schema = ListSchema()

        return schema.dump(list), 200

    # list/<int:list_id>
    def delete(self, list_id): 
        user_id = get_jwt_identify()
        validate_user_id (user_id)

        list = List.query.filter_by(id = list_id).first()

        if not list:
            return {"Error":"List not found"}, 404

        list.delete()
        
        return {"Status":"List deleted"}, 200