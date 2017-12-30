from flask_login import UserMixin

from app.database import db
from app.models.base import BaseModel


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)


