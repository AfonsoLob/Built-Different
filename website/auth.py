from flask import Blueprint, render_template, request, redirect, url_for
from .database import verify_user, add_user, get_user_password
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

        if(len(email) < 4):
            return '<h1>Email not valid. Need more than 3 characters</h1>'
        elif(password != password_confirm):
            return '<h1>Password does not match</h1>'
        elif(len(password) < 8):
            return '<h1>Password needs to have more than 7 characters</h1>'
        else:
            # add user to database (if email not in use)
            new_user = User(username, email, generate_password_hash(password, method="sha256"))
            # utilizar generate hash na database ao inves de aqui
            value = verify_user(email)
            if(value == False): # User can be created
                add_user(email, password, username)
                return redirect(url_for('views.home'))
            else:
                return "<h1>Email already in use<h1>"
        
    return render_template('sign_up.html')