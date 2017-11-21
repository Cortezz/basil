from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_tables():
    db.create_all()


def drop_tables():
    db.reflect()
    db.drop_all()
