# This is not an excutable code block
from flask import Flask

app = Flask("myapp")

@app.route('/')
def hello_world():
    return 'Hello, World!'


# This is not an excutable code block
from flask import Flask

app = Flask("myapp")

@app.route('/')
def hello_world():
    return 'Hello, World!'

$ flask --app hello run
#  * Serving Flask app 'hello'
#  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
#==================================================================
#     EXAMPLE
#==================================================================
from flask import Flask

app = Flask("hello")
@app.route('/hello/<name>')

def hello_world(name):
    return f'Hello, {name}!'
