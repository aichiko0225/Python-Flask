from sayhello import app, db
from sayhello.commands import forge, initdb


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8888)
