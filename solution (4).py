from flask import Flask, render_template, redirect, url_for
import datetime
from forms import Form

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


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    form = Form()
    if form.validate_on_submit():
        ans = {'title': 'Заголовок',
               'surname': form.surname.data,
               'name': form.name.data,
               'education': form.education.data,
               'profession': form.profession.data,
               'sex': form.sex.data,
               'motivation': form.motivation.data,
               'ready': form.ready.data}
        return redirect(url_for('/auto_answer', ans=ans))
    return render_template('answer.html', form=form)


@app.route('/auto_answer/<ans>')
def auto_answer(ans):
    return render_template('answer.html', ans=ans)


app.run()