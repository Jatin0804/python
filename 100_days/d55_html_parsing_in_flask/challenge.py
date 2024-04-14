from flask import Flask
app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b> {func()} </b>"

    return wrapper

def make_italic(func):
    def wrapper():
        return f"<em> {func()} </em>"

    return wrapper

def make_underline(func):
    def wrapper():
        return f"<u> {func()} </u>"

    return wrapper

# change html tags
@app.route('/')
def hello_world():
    return "<h1> Hello World! </h1>"

@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye_world():
    return "Bye world"

if __name__ == '__main__':
    app.run(debug=True)