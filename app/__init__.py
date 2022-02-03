from flask import Flask
from app.extensions import db, migrate, ma, jwt

from users.routes import user_api

def create_app():
    app = Flask(__name__)
    
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(user_api)

    return app