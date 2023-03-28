from flask import Blueprint, render_template, redirect, url_for
from .auth import session

views = Blueprint('views', __name__)

# Routes for blueprint views
@views.route('/', methods=['GET','POST'])
def home():
    if('username' in session):
        return render_template('index.html')
    else:
        return redirect( url_for('auth.login') )

 