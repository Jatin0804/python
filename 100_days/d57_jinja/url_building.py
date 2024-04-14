from flask import Flask, render_template
app = Flask(__name__)
import requests

import random
import time

@app.route('/')
def home():
    random_number = random.randint(1, 100)
    year = time.strftime("%Y")
    return render_template("url_building.html", random_number=random_number, year = year)

@app.route("/blog/<num>")
def get_blog(num):
    BLOG_LINK =  "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(BLOG_LINK)
    blog_data = response.json()
    return render_template("blog_try.html", posts=blog_data)


if __name__ == '__main__':
    app.run(debug=True)