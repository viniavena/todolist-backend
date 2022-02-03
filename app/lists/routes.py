from flask import Blueprint
from .controllers import ListFunctions

list_api = Blueprint('list_api', __name__)

# Add To Do
list_api.add_url_rule(
    '/list/new',
    view_func = ListFunctions.as_view('add_list'),
    methods = ['POST'],
)

# Edit To Do
list_api.add_url_rule(
    '/list/<int:list_id>',
    view_func = ListFunctions.as_view('get_list'),
    methods = ['GET'],
)

# Delte To Do
list_api.add_url_rule(
    '/list/<int:list_id>/delete',
    view_func = ListFunctions.as_view('delete_list'),
    methods = ['DELETE'],
)
