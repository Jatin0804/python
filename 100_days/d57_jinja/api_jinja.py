from flask import Flask, render_template
app = Flask(__name__)

import requests

LINK1 = "https://api.agify.io/?name="
LINK2 = "https://api.genderize.io/?name="
def fetch(name):
    link1 = LINK1 + name
    link2 = LINK2 + name
    response1 = requests.get(link1)
    response2 = requests.get(link2)
    # print(response.text)
    return [response1.json(), response2.json()]


@app.route("/")
def home():
    return "Go to localhost:5000/guess/{name}"

@app.route("/guess/<name>")
def guess(name):
    response1, response2 = fetch(name)
    name = response1["name"]
    age = response1["age"]
    gender = response2["gender"]
    return render_template("api_jinja.html", name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)