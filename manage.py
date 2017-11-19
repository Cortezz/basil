from flask_script import Manager

import os

from app import create_app


app = create_app(os.environ.get('APP_ENV'))
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
