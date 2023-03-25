from flask import Blueprint, render_template, request, redirect, url_for
from .database import verify_user, add_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

# Routes related with authentication
@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('views.home'))
        
    else:
        return render_template('login.html')



@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password1']
        password_confirm = request.form['password2']
        username = request.form['username']

        if(len(email) < 4):
            pass
        elif(password != password_confirm):
            pass
        elif(len(password) < 8):
            pass
        else:
            # add user to database (if email not in use)
            new_user = User(username, email, generate_password_hash(password, method="sha256"))
            value = verify_user(email)
            if(value == True): # User is available
                add_user(email, password, username)
                return redirect(url_for('views.home'))
            else:
                return "<h1>Email already in use<h1>"
        
    return render_template('sign_up.html')