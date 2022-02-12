from flask import Flask, render_template, redirect
import datetime
from forms import Form, SecurityForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def main():
    title = 'Заготовка'
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/login')
def login():
    form = SecurityForm()
    return render_template('login.html', form=form)


app.run()