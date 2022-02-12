from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизации Марса'


@app.route('/index')
def main():
    return 'И на Марсе будут яюлони цвести!'


@app.route('/promotion')
def promotion():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return '</br>'.join(text)


@app.route('/image_mars.')
def image_mars():
    return f'''<!DOCTYPE html>
                <head> <title>Привет, Марс!</title>
                </head>
                <body><h1>Жди нас, Марс!</h1></br>
                <img src="{url_for('static', filename='img/MARS.png')}"/>
                <p>Вот она какая, красная планета</p>
                </body>'''


@app.route('/promotion_image')
def promotion_image():
    text = ['<p style="background-color: grey">Человечество вырастает из детства.</p>',
            '<p style="background-color: green">Человечеству мала одна планета.</p>',
            '<p style="background-color: grey">Мы сделаем обитаемыми безжизненные пока планеты.</p>',
            '<p style="background-color: yellow">И начнем с Марса!</p>',
            '<p style="background-color: red">Присоединяйся!</p>']
    return f'''<!DOCTYPE html>
                    <head> <title>Колонизация</title>
                    </head>
                    <body><h1 style="color:red">Жди нас, Марс!</h1></br>
                    <img src="{url_for('static', filename='img/MARS.png')}"/>
                    <p>Вот она какая, красная планета</p>
                    {''.join(text)}
                    </body>'''


app.run(host='127.0.0.1', port=8080)