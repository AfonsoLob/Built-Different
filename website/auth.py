from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# Routes related with authentication
@auth.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"