from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from models.user_model import User
