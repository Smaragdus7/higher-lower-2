import random
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/10vk5L8tHKN1UQ/giphy.gif">'


RANDOM_NUMBER = random.randint(0, 9)


@app.route('/<int:number>')
def check_number(number):
    if number < RANDOM_NUMBER:
        return '<h1 style="color:red">Too low!</h1>' \
               '<img src="https://media.giphy.com/media/1SvnHJFEuEH7hp81tF/giphy.gif">'
    elif number > RANDOM_NUMBER:
        return '<h1 style="color:green">Too high!</h1>' \
               '<img src="https://media.giphy.com/media/mPJ4VPpXPtYuA/giphy.gif">'
    else:
        return '<h1 style="color:purple">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/AhiEIIwVg7CQE/giphy.gif">'

