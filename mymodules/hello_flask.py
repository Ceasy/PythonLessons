from flask import Flask
import vowels2

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello Aleksey, from Flask!'


@app.route('/search')
def do_search() -> str:
    return str(vowels2.search4letters('life, the universe, ans everything', 'eiru,!'))

@app.route('/evelina')
def a_fun() -> str:
    return str(vowels2.search4letters(input('pls, enter prase: '), input('pls, enter letters: ')))


@app.route('/shikaka')
def shikaka() -> str:
    return {'0Name': 'Evelina'}
app.run()
