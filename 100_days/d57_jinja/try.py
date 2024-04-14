from flask import Flask, render_template
app = Flask(__name__)

import random
import time

@app.route('/')
def home():
    random_number = random.randint(1, 100)
    year = time.strftime("%Y")
    return render_template("try.html", random_number=random_number, year = year)

if __name__ == '__main__':
    app.run(debug=True)