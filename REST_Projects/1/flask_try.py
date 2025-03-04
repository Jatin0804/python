from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hithere')
def hi_there():
    return 'Hi there isnetad of hello world'

if __name__ == '__main__':
    app.run()