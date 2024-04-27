from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "secret-key"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('/new/index_new.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.email.data == 'try@email.com' and login_form.password.data == '1234':
            return render_template("/new/success_new.html")
        else:
            return render_template("/new/denied_new.html")

    return render_template("/new/login_new.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
