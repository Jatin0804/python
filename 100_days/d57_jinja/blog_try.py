from flask import Flask, render_template
app = Flask(__name__)
import requests

@app.route("/")
def home():
    return "Go to localhost:5000/blog"

@app.route("/blog")
def blog():
    BLOG_LINK =  "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(BLOG_LINK)
    blog_data = response.json()
    return render_template("blog_try.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)