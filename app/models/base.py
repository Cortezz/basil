import uuid
import datetime

from sqlalchemy_utils import UUIDType
from flask_sqlalchemy import event, SessionBase
from flask import current_app

from app.database import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUIDType(binary=False), primary_key=True)

    created_at = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.Float, nullable=True)

    def reload(self):
        db.session.refresh(self)

    def save(self):
        db.session.commit()

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_all(cls):
        try:
            db.session.query(cls).delete()
            db.session.commit()
        except Exception as e:
            current_app.logger.info(e)
            db.rollback()
        return



@event.listens_for(SessionBase, "before_flush")
def before_flush_handler(session, flush_context, instances):
    for obj in session.new:
        obj.id = uuid.uuid1()
        obj.created_at = datetime.datetime.utcnow().timestamp()

    for obj in session.dirty:
        obj.updated_at = datetime.datetime.utcnow().timestamp()
