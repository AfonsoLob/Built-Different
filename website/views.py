from flask import Blueprint, render_template, redirect, url_for, request
from .auth import session
from .database import verify_user_stats, create_user_stats, get_stats, update_stats, update_gender, update_objective, update_activity, get_type
from .database import add_plan, get_plans
import json

views = Blueprint('views', __name__)

# Routes for blueprint views
@views.route('/', methods=['GET','POST'])
def home():
    if('user' in session):
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
        elif(request.form['op'] == '1'):
            gender = request.form['gender']
            update_gender(email, gender)
        elif(request.form['op'] == '2'):
            objective = request.form['objective']
            update_objective(email, objective)
        elif(request.form['op'] == '3'):
            activity = request.form['activity']
            update_activity(email, activity)
        
        stats = get_stats(email)
        # print(stats)
        return "done"
    else:
        if('user' in session):
            username = session['user']['username']
            email = session['user']['email']
            if (verify_user_stats(email) == False): create_user_stats(email)
            stats = get_stats(email)
            return render_template('profile.html', username=username, email=email, age=stats['age'], height=stats['height'], weight=stats['weight'],
                                    gender=stats['gender'], objective=stats['objective'], activity=stats['activity'], type=get_type(email))
        else:
            return redirect( url_for('auth.login') )

@views.route('/plans', methods=['GET', 'POST'])
def view_plans():
    if request.method == 'POST':
        username = session['user']['username']
        treino = request.form['treino']
        tipo   = request.form['tipo']
        dificuldade = request.form['dificuldade']
        num_of_sets = request.form['number_of_sets']
        set_reps = request.form['sets_reps']
        exercises = request.form['exercises']
        descansos = request.form['descansos']

        add_plan(treino, username, tipo, dificuldade, num_of_sets, 
                 set_reps, exercises, descansos) # json.dumps() não é usado pois a lista já é recebida em formato String
    
        return "done"
    else:
        if('user' in session):
            email = session['user']['email']
            plans = get_plans()
            plans = list(plans)
            for i in range(len(plans)):
                plans[i] = list(plans[i])
                plans[i][6] = json.loads(plans[i][6]) # Turn ListString to List
                plans[i][7] = json.loads(plans[i][7])
                plans[i][8] = json.loads(plans[i][8])
                plans[i] = tuple(plans[i])
                
            plans = tuple(plans)
            return render_template('plans.html', type=get_type(email), plans=plans)
        else:
            return redirect( url_for('auth.login') )
    
@views.route('/personal_trainers', methods=['GET'])
def personal_trainers():
    if('user' in session):
        email = session['user']['email']
        return render_template('personal_trainers.html', session_user = email, userType = get_type(email))
    else:
        return redirect( url_for('auth.login'))
    
@views.route('/nutritionists', methods=['GET'])
def nutrionists():
    if('user' in session):
        email = session['user']['email']
        return render_template('nutritionists.html', session_user = email, userType = get_type(email))
    else:
        return redirect( url_for('auth.login'))
    
@views.route('/classes', methods=['GET'])
def classes():
    if('user' in session):
        return render_template('classes.html')
    else:
        return redirect( url_for('auth.login'))