from flask import Flask
from dotenv import load_dotenv, find_dotenv
from routes import routes_blueprint

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run()
