from flask import Flask, render_template
app = Flask(__name__)
import requests

LINK = "https://api.npoint.io/eaa0e46949ed3681c81a"
posts = requests.get(LINK).json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested = None
    for blog in posts:
        if blog["id"] == index:
            requested = blog
    return render_template("post.html", post=requested)

if __name__ == '__main__':
    app.run(debug=True, port=5001)