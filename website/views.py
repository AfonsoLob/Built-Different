from flask import Blueprint, render_template, redirect, url_for, request
from .auth import session
from .database import verify_user_stats, create_user_stats, get_stats, update_stats, update_gender, update_objective

views = Blueprint('views', __name__)

# Routes for blueprint views
@views.route('/', methods=['GET','POST'])
def home():
    try:
        id = request.args['id']
    except:
        return redirect( url_for('auth.login'))
    if(id in session):
        print(session)
        return render_template('index.html')
    else:
        return redirect( url_for('auth.login') )

@views.route('/profile', methods=['GET', 'POST'])
def user_profile():
    if request.method == 'POST':
        print(request.form)
        email = request.form['email']
        if(request.form['op'] == '0'):
            age = request.form['idade']
            height = request.form['altura']
            weight = request.form['peso']
            update_stats(email, age, height, weight)
        if(request.form['op'] == '1'):
            gender = request.form['gender']
            update_gender(email, gender)
        else:
            objective = request.form['objective']
            update_objective(email, objective)
        
        stats = get_stats(email)
        print(stats)
        return "done"
    else:
        id = request.args['id']
        if(id in session):
            username = session[id]['username']
            email = session[id]['email']
            if (verify_user_stats(email) == False): create_user_stats(email)
            stats = get_stats(email)
            print(stats)
            return render_template('profile.html', username=username, email=email, age=stats['age'], height=stats['height'], weight=stats['weight'], gender=stats['gender'], objective=stats['objective'] )
        else:
            return redirect( url_for('auth.login') )

@views.route('/plans', methods=['GET', 'POST'])
def view_plans():
    if request.method == 'POST':
        print(request.form)
        return "done"
    else:
        if('username' in session):
            return render_template('plans.html')
        else:
            return redirect( url_for('auth.login') )
    