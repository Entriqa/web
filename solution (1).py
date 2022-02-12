from flask import Flask, render_template, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def main():
    title = 'Заготовка'
    return render_template('base.html', title=title)


app.run()