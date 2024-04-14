from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_obs = []
for post in posts:
    post_obs.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

@app.route('/')
def get_all_posts():
    return render_template("bootstrap_try.html", all_posts=post_obs)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested = None
    for blog_post in post_obs:
        if blog_post.id == post_id:
            requested = blog_post
    return render_template("post.html", post=requested)

if __name__ == "__main__":
    app.run(debug=True)
