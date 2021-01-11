from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for, render_template, flash
from forms import LoginForm, RegistrationForm



app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/flaskblog2'
# db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/account")
def contact():
    return render_template('account.html', title='Account')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    return render_template('home.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)