from flask import Flask
app = Flask(__name__)


# change html tags
@app.route('/')
def hello_world():
    return "<h1> Hello World! </h1>"

# change multiple html tags
@app.route('/hi')
def hello_world1():
    return ("<h1> Hello World! </h1>"
            "<p>This is another paragraph </p>"
            "<img src='https://th.bing.com/th/id/OIP.DGu9im2kr0eKsYb4EkI7ZQHaEo?rs=1&pid=ImgDetMain' width=500px>"
            "<img src='https://media4.giphy.com/media/00xGP4zv8xENZ2tc3Y/200w.webp' width=500px>")

# change in-style css
@app.route('/bye')
def bye_world():
    return "<h1 style = 'text-align: center'> Bye world </h1>"

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}"

# variable path
@app.route('/user/<username>')
def hello_user(username):
    return f"Hello there {username}"

# change datatype
@app.route('/user/<username>/<int:number>')
def hello_number(username, number):
    return f"Hello {username}, your number is {number}"

if __name__ == '__main__':
    app.run(debug=True)