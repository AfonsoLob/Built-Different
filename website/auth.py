from flask import Blueprint, render_template, request, redirect, url_for
from .database import verify_user, add_user, get_user_password
from werkzeug.security import generate_password_hash, check_password_hash
import re # used to validate email
regex = '^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$'  
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
        value = verify_user(email)
        if (value == True):
            # Verify if password is correct
            if check_password_hash(get_user_password(email), password):
                return redirect(url_for('views.home'))
            else:
                return '<h1>Incorrect Password</h1>'
            
        else:
            return '<h1>Email does not exist</h1>'
        
    else:
        return render_template('login.html')



@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password1']
        password_confirm = request.form['password2']
        username = request.form['username']
        errors = {}
        error_regist = 0
        if(re.search(regex, email) == None):
            errors["email"] = 1
            error_regist = 1
        elif(len(password) < 8):
            errors["plength"] = 1
            error_regist = 1
        elif(password != password_confirm):
            errors["pconfirm"] = 1
            error_regist = 1
        if(error_regist == 0):
            value = verify_user(email)
            if(value == False): # User can be created
                add_user(email, password, username)
                return redirect(url_for('views.home'))
            else:
                return "<h1>Email already in use<h1>"
        return render_template('sign_up.html', errors=errors, email=email, username=username)
        
    else:
        return render_template('sign_up.html')