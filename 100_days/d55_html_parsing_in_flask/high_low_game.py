from flask import Flask
app = Flask(__name__)
from random import randint

random_number = randint(0, 9)
def make_bold(func):
    def wrapper():
        return f"<b> {func()} </b>"

    return wrapper


@app.route('/')
@make_bold
def base_link():
    return ("<h1 style='color: black; text-align: center'> Guess a number between 0 and 9 </h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route('/<int:guess>')
def number_link(guess):
    if guess > random_number:
        return "<h1 style='color: purple; text-align: center'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    elif guess < random_number:
        return "<h1 style='color: red; text-align: center'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color: green; text-align: center'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)