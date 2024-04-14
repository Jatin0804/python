from flask import Flask
app = Flask(__name__)
from random import randint

LOW_URL = "https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif"
HIGH_URL = "https://media.giphy.com/media/27sdoZn8YhLbil01q6/giphy.gif"
CORRECT_URL = "https://media.giphy.com/media/uVpPvvpU3nip5pBkPD/giphy.gif"
GUESS_NUMBER_URL = "https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy-downsized-large.gif"

TOO_HIGH_STYLE = 'style="color:red; text-align:center;"'
TOO_LOW_STYLE = 'style="color:blue; text-align:center;"'
CORRECT_STYLE = 'style="color:green; text-align:center;"'
GUESS_STYLE = 'style="color:black; text-align:center;"'


def h1_tag_decorator(function):
    def wrapper(*args, **kwargs):
        return f" <h1><b>{function(args[0])} </b></h1> "
    return wrapper


def create_img(function):
    def wrapper(*args, **kwargs):
        return f'<img src="{function(args[0])}" style="max-width: 100%;">'

    return wrapper


def center_img_decorator(function):
    def wrapper(*args, **kwargs):
        return f"<center>{function(args[0])}</center>"
    return wrapper


def make_bold(func):
    def wrapper(*args, **kwargs):
        return "<h1><b>" + func(args[0]) + "</b></h1>"

    return wrapper


@center_img_decorator
@create_img
def add_image(image):
    return image


@h1_tag_decorator
@make_bold
def response(text):
    return text


def combine_strings(func1, func2):
    return f"{func1}{func2}"


def add_css(string, css):
    index = string.find(">")
    output = string[:index] + " " + css + "" + string[index:]
    print(output)
    return output


def check_res(num):
    if num > random_number:
        text = "Too high!!"
        gif_url = HIGH_URL
        css_styling = TOO_HIGH_STYLE
    elif num < random_number:
        text = "Too low!!!"
        gif_url = LOW_URL
        css_styling = TOO_LOW_STYLE
    else:
        text = "That is correct!!!"
        gif_url = CORRECT_URL
        css_styling = CORRECT_STYLE

    string = combine_strings(response(text), add_image(gif_url))
    return add_css(string, css_styling)


@app.route("/")
def home_page():
    text = "Guess a number between 0 and 9"
    string = combine_strings(response(text), add_image(GUESS_NUMBER_URL))
    return add_css(string, GUESS_STYLE)


@app.route("/<int:guess_number>")
def show(guess_number):
    return check_res(guess_number)


if __name__ == "__main__":
    random_number = randint(0, 9)
    app.run(debug=True)


# def generate_num(function):
#     def wrapper(*args, **kwargs):
#         if args[0] == num:
#             return (f"<h1>Your found meee.</h1>"
#                     f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
#         if args[0] < num:
#             return (f"<h1>Your number is low</h1>"
#                     f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
#         if args[0] > num:
#             return (f"<h1>Your number is high</h1>"
#                     f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
#     return wrapper