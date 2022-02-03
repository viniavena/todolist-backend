from flask import Blueprint
from .controllers import ToDoFunctions

todo_api = Blueprint('todo_api', __name__)

# Add To Do
todo_api.add_url_rule(
    '/todo/new/<int:list_id>',
    view_func = ToDoFunctions.as_view('add_todo'),
    methods = ['POST'],
)

# Edit To Do
todo_api.add_url_rule(
    '/todo/<int:todo_id>/edit',
    view_func = ToDoFunctions.as_view('edit_todo'),
    methods = ['PATCH'],
)

# Delte To Do
todo_api.add_url_rule(
    '/todo/<int:todo_id>/delete',
    view_func = ToDoFunctions.as_view('delete_todo'),
    methods = ['DELETE'],
)
