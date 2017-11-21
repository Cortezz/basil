from app.database import db
from .base import BaseModel


class Trip(BaseModel):
    __tablename__ = 'trip'

    name = db.Column(db.String, nullable=True)
    coordinates = db.Column(db.JSON, nullable=False)
