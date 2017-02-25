from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from routes import routes_blueprint
import os

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run()
