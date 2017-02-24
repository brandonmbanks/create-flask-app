from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == "__main__":
    app.run()
