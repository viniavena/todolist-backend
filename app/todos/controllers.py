from flask import request, abort, make_response, jsonify
from flask.views import MethodView
from marshmallow_sqlalchemy import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from .model import ToDo
from .schema import ToDoSchema
from ..lists.model import List
from ..lists.controllers import validate_user_id
from ..users.model import User

class ToDoFunctions(MethodView):

    decorators = [jwt_required()]

    def post(self, list_id): # /todo/new/<int:list_id>

        user_id = get_jwt_identity()
        user =  validate_user_id(user_id)

        list = List.query.get_or_404(list_id)

        data = request.json

        schema = ToDoSchema()

        try:
            todo = schema.load(data)
        except ValidationError as err:
            abort(
                make_response(
                    err.messages, 400
                )
            )

        todo.list = list

        todo.save()
        list.update()

        return ToDoSchema().dump(todo), 200