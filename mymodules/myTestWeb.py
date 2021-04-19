from flask import Flask, render_template, request
import mymoduletest1

app = Flask(__name__)


@app.route('/start', methods=['POST', 'GET'])
@app.route('/')
def hello() -> str:
    return render_template('myEntry.html',
                           the_title='It is my simple beta calculate!')


@app.route('/res', methods=['POST', 'GET'])
def sum():
    number_1 = request.form['number_1']
    number_2 = request.form['number_2']
    action = request.form['action']
    title = 'Here you are result:'
    result = str(mymoduletest1.sum_function(float(number_1), float(number_2), action))
    if result == '-991':
        return render_template('myErrorAction.html',
                               the_title='Sorry, you entered incorrect data')
    else:
        return render_template('myresult.html',
                               the_number_1=number_1,
                               the_number_2=number_2,
                               the_action=action,
                               the_title=title,
                               the_result=result)


if __name__ == '__main__':
    app.run(debug=True)

