from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def static_try():
    return render_template('try_html.html')

if __name__ == '__main__':
    app.run(debug=True)