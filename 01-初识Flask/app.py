from flask import Flask, redirect, url_for, abort, make_response, json
from flask import jsonify, request, session

app = Flask(__name__)
app.secret_key = 'Drmhze6EPcv0fN_81Bj-nA'


@app.before_request
def do_something():
    # 这里的代码会在每个请求处理前执行
    print(request.cookies)
    pass


# name = request.cookies.get('name', default='Human')


@app.route('/login')
def login():
    # 写入session
    session['logged_in'] = True
    response = make_response(redirect(url_for('say_hello')))
    response.set_cookie('name', 'ash')
    return response


@app.route('/foo')
def foo():
    response = make_response('Hello, World!')
    response.mimetype = 'text/plain'
    return response


@app.route('/foo_json')
def foo_json():
    data = {
         'name': 'Grey Li', 'gender': 'male'
        }
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/foo_json_1')
def foo_json_1():
    return jsonify(name='Grey Li', gender='male')


@app.route('/404')
def not_found():
    abort(404)


@app.route('/')
def index():
    return '<h1>hello world!</h1>', 201


@app.route('/helloss')
def say_helloss():
    return redirect(url_for('say_hello'))


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greetname(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/red')
@app.route('/red/<name>')
def greet(name='Programmer'):
    return '<h1>Hello, %s!</h1>' % name


# @app.route('goback/<int:year>')
# def go_back(year):
#     return '<p>Welcome to %d!</p>' % (2018 - year)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8888
    )
