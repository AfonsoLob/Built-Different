from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# Routes for blueprint views

@views.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')


 