from crypt import methods
from flask import Blueprint
from .controllers import UserCreate, UserCurrent, TestHealth

user_api = Blueprint('user_api', __name__)

# Current User
user_api.add_url_rule(
    '/user/',
    view_func = UserCurrent.as_view('current_user'),
    method = ['GET']
)

# Sign Up
user_api.add_url_rule(
    '/signup',
    view_func = UserCreate.as_view('sign_up'),
    methods = ['POST']
)

# Test Health
user_api.add_url_rule(
    '/ping',
    view_func = TestHealth.as_view('test'),
    methods = ['GET']
)