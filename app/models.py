from sqlalchemy.exc import IntegrityError
from flask import abort, jasonify, make_response
from .extensions import db


class BaseModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime(timezone=True), server_default = db.func.now())
    update_time = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(make_response(jasonify({'errors':str(err.orig)}),400))

    def update(self):
        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(make_response(jasonify({'errors':str(err.orig)}),400))

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(make_response(jasonify({'errors':str(err.orig)}),400))