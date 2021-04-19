from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello, Aleksey!'

@app.route('/a')
def my_fun() -> str:
    return 'decorator fun is'+ app.route.__name__

app.run()
