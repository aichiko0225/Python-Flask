from flask import Flask, render_template, redirect, url_for,flash
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'Drmhze6EPcv0fN_81Bj-nA'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/form_1')
def form_1():
    return render_template('form_1.html')


@app.route('/basic', methods=['GET', 'POST'])
def basic():
    form = LoginForm()
    if form.validate():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/bootstrap', methods=['GET', 'POST'])
def bootstrap():
    form = LoginForm()
    if form.validate():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('bootstrap.html', form=form)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8888
    )
