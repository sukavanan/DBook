from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo

from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'dbook'
app.config['MONGO_URI'] = 'mongodb://shree:strongpassword123@ds060369.mlab.com:60369/dbook'
app.config['SECRET_KEY'] = '97542ec161edf850af891551159ea600'
mongo = PyMongo(app)

@app.route('/')
def index_route():
    if 'username' in session:
        return f'You are logged in as {session["username"]}!'
    
    return render_template('index.html', align_center=True)

@app.route('/login', methods = ['GET', 'POST'])
def login_route():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register_route():
    form = RegistrationForm()
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)