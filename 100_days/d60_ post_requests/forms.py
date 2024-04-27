from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("forms.html")

@app.route("/login", methods=["POST"])
def login():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Welcome: {name} !, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)