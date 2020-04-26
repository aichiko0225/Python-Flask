from bluelog import create_app  # noqa
import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

config_name = os.getenv('FLASK_CONFIG')

print(config_name)

app = create_app('development')

if __name__ == "__main__":
    app.run(debug=True, port=8888)
