from flask import Flask
from dotenv import load_dotenv, find_dotenv
from routes import routes_blueprint
import os

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run()
