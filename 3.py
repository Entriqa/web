from flask import Flask, render_template, redirect
import datetime
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def main():
    title = 'Заготовка'
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер', 'строитель', 'врач', 'программист']
    return render_template('list_prof.html', list=list, prof=profs)


app.run()