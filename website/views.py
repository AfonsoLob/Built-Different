from flask import Blueprint, render_template, redirect, url_for, request
from .auth import session
from .database import verify_user_stats, create_user_stats, get_stats, update_stats, update_gender, update_objective, update_activity

views = Blueprint('views', __name__)

# Routes for blueprint views
@views.route('/', methods=['GET','POST'])
def home():
    if('user' in session):
        print(session)
        return render_template('index.html')
    else:
        return redirect( url_for('auth.login') )

@views.route('/profile', methods=['GET', 'POST'])
def user_profile():
    if request.method == 'POST':
        # print(request.form)
        email = request.form['email']
        if(request.form['op'] == '0'):
            age = request.form['idade']
            height = request.form['altura']
            weight = request.form['peso']
            update_stats(email, age, height, weight)
        elif(request.form['op'] == '1'):
            gender = request.form['gender']
            update_gender(email, gender)
        elif(request.form['op'] == '2'):
            objective = request.form['objective']
            update_objective(email, objective)
        elif(request.form['op'] == '3'):
            activity = request.form['activity']
            update_activity(email, activity)
        
        # stats = get_stats(email)
        # print(stats)
        return "done"
    else:
        if('user' in session):
            username = session['user']['username']
            email = session['user']['email']
            if (verify_user_stats(email) == False): create_user_stats(email)
            # stats = get_stats(email)
            # print(stats)
            return render_template('profile.html', username=username, email=email, age=stats['age'], height=stats['height'], weight=stats['weight'], gender=stats['gender'], objective=stats['objective'], activity=stats['activity'] )
        else:
            return redirect( url_for('auth.login') )

@views.route('/plans', methods=['GET', 'POST'])
def view_plans():
    if request.method == 'POST':
        # print(request.form)
        return "done"
    else:
        if('user' in session):
            return render_template('plans.html')
        else:
            return redirect( url_for('auth.login') )
    
@views.route('/team', methods=['GET'])
def team():
    if('user' in session):
        return render_template('team.html')
    else:
        return redirect( url_for('auth.login'))