from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("contact.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        print(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


if __name__ == '__main__':
    app.run(debug=True, port=5001)