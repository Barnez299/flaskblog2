from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for, render_template, flash
from forms import LoginForm, RegistrationForm



app = Flask(__name__)

app.config['SECRET_KEY'] = 'fb1a97349eaa6286b0d65b08bcdf6917'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/flaskblog2'
# db = SQLAlchemy(app)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Frank Doe',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'April 25, 2018'
    },
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/account")
def account():
    return render_template('account.html', title='Account')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@mail.me' and form.password.data =='password':
            flash(f'Log in successfull.', category='success')
            return redirect(url_for('account'))
        else:
            flash(f'Please check user details!', category='danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)