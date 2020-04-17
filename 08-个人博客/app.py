# from sayhello import app, db
# from sayhello.commands import forge, initdb


# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True, port=8888)

import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

config_name = os.getenv('FLASK_CONFIG')

print(config_name)
