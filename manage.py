from flask_script import Manager

import os

from app import create_app


app = create_app(os.environ.get('APP_ENV'))
manager = Manager(app)

@manager.command
def create_db():
    from app.database import create_tables
    create_tables()


@manager.command
def drop_db():
    from app.database import drop_tables
    drop_tables()


@manager.command
def reset_db():
    from app.database import create_tables, drop_tables
    drop_tables()
    create_tables()


if __name__ == "__main__":
    manager.run()
