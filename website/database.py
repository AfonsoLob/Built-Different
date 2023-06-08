import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
import json

DB_STRING = "database.db"

db_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(db_directory, DB_STRING)

def setup_database():
    user_table = """ CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        username TEXT NOT NULL,
        type TEXT,
        plansId TEXT
    );"""
    user_stats = """ CREATE TABLE IF NOT EXISTS user_stats (
        email TEXT NOT NULL,
        age TEXT NOT NULL,
        height TEXT NOT NULL,
        weight TEXT NOT NULL,
        gender TEXT,
        objective TEXT,
        activity TEXT
    );"""
    add_worker1 = f""" INSERT OR IGNORE INTO users (email, password, username,type)
        VALUES ('personal1@ua.pt','{generate_password_hash('personalTrainer')}','Nuno Oliveira', '0');
        """
    add_worker2 = f""" INSERT OR IGNORE INTO users (email, password, username,type)
        VALUES ('personal2@ua.pt','{generate_password_hash('personalTrainer')}','Ramon Dino', '0');
        """
    add_worker3 = f""" INSERT OR IGNORE INTO users (email, password, username,type)
        VALUES ('personal3@ua.pt','{generate_password_hash('personalTrainer')}','Ronnie Coleman', '0');
        """
    add_worker4 = f""" INSERT OR IGNORE INTO users (email, password, username,type)
        VALUES ('nutricionista1@ua.pt','{generate_password_hash('nutricionista')}','Nutricionista 1', '1');
        """
    add_worker5 = f""" INSERT OR IGNORE INTO users (email, password, username,type)
        VALUES ('nutricionista2@ua.pt','{generate_password_hash('nutricionista')}','Nutricionista 2', '1');
        """
    add_worker6 = f""" INSERT OR IGNORE INTO users (email, password, username,type)
        VALUES ('nutricionista3@ua.pt','{generate_password_hash('nutricionista')}','Nutricionista 3', '1');
        """
    plans_table = """ CREATE TABLE IF NOT EXISTS plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        owner TEXT NOT NULL,
        type TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        number_of_sets TEXT NOT NULL,
        sets_reps TEXT NOT NULL,
        exercises TEXT NOT NULL,
        descansos TEXT NOT NULL
    );"""
    # trainings_table = """ CREATE TABLE IF NOT EXISTS trainings (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     training_name TEXT NOT NULL UNIQUE,
    #     previous_owner_id INTEGER,
    #     ts TEXT NOT NULL,
    #     image_id INTEGER NOT NULL,
    #     FOREIGN KEY (current_owner_id) REFERENCES users (id),
    #     FOREIGN KEY (previous_owner_id) REFERENCES users (id),
    #     FOREIGN KEY (image_id) REFERENCES images (image_id)
    # );
    # """

    with sqlite3.connect(db_path) as con:
        con.execute(user_table)
        con.execute(user_stats)
        con.execute(plans_table)
        con.execute(add_worker1)
        con.execute(add_worker2)
        con.execute(add_worker3)
        con.execute(add_worker4)
        con.execute(add_worker5)
        con.execute(add_worker6)


def cleanup_database():
    users_table = "DROP TABLE IF EXISTS users;"
    users_stats = "DROP TABLE IF EXISTS user_stats;"
    plans_table = "DROP TABLE IF EXISTS plans;"
    with sqlite3.connect(db_path) as con:
        # con.execute(users_table)
        # con.execute(users_stats)
        con.execute(plans_table)

def verify_user(user_email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
            SELECT email FROM users;
        """)
        list_of_emails = cur.fetchall()
        for email in list_of_emails:
            email = email[0]
            if (email == user_email): 
                return True
        return False
    
def get_user_password(email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
        SELECT password FROM users
        WHERE email = '{email}';
        """)
        user_password = cur.fetchall()[0]        
        return user_password[0]
    
def update_password(email, new_password):
    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        UPDATE users
        SET password = '{generate_password_hash(new_password)}'
        WHERE email = '{email}';
        """)
    
def get_username(email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
        SELECT username FROM users
        WHERE email = '{email}';
        """)
        username = cur.fetchall()[0]
        return username[0]
    
def get_id(email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
        SELECT id FROM users
        WHERE email = '{email}';
        """)
        id = cur.fetchall()[0]
        return id[0]
    
def add_user(email, password, username):
    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        INSERT INTO users (email, password, username)
        VALUES ('{email}','{generate_password_hash(password)}','{username}');
        """)

def verify_user_stats(user_email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
            SELECT email FROM user_stats;
        """)
        list_of_emails = cur.fetchall()
        for email in list_of_emails:
            email = email[0]
            if (email == user_email): 
                return True
        return False
    
def get_stats(email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT age,height,weight,gender,objective,activity FROM user_stats
            WHERE email = '{email}';
            """)
        list_of_stats = cur.fetchall()[0]
        return {'age': list_of_stats[0], 'height': list_of_stats[1], 'weight': list_of_stats[2], 'gender': list_of_stats[3], 'objective': list_of_stats[4], 'activity': list_of_stats[5]}
        
def get_type(email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT type FROM users
            WHERE email = '{email}';
            """)
        type = cur.fetchall()[0][0]
        return type

def create_user_stats(email):
    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        INSERT INTO user_stats (email, age, height, weight)
        VALUES ('{email}', '#', '#' , '#');
        """)

def update_stats(email, age, height, weight):
    if(age.isdigit() == False): age = '#'
    if(height.isdigit() == False): height = '#'
    if(weight.isdigit() == False): weight = '#'

    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        UPDATE user_stats
        SET age = '{age}',
            height = '{height}',
            weight = '{weight}'
        WHERE email = '{email}';
        """)

def update_gender(email, gender):
    if(gender == "Masculino"): gender = 1
    elif(gender == "Feminino"): gender = 0
    else: return

    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        UPDATE user_stats
        SET gender = '{gender}'
        WHERE email = '{email}';
        """)

def update_objective(email, objective):
    if(objective == "Bulk"): objective = 0
    elif(objective == "Maintain"): objective = 1
    elif(objective == "Cut"): objective = 2
    else: return

    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        UPDATE user_stats
        SET objective = '{objective}'
        WHERE email = '{email}';
        """)

def update_activity(email, activity):
    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        UPDATE user_stats
        SET activity = '{activity}'
        WHERE email = '{email}';
        """)

def get_plans():
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
        SELECT * FROM plans;            
        """)
        data = cur.fetchall()

        return data

def add_plan(category, owner, type, difficulty, number_of_sets, set_reps, exercises, descansos):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
        INSERT INTO plans (category, owner, type, difficulty, number_of_sets, sets_reps, exercises, descansos)
        VALUES ('{category}','{owner}','{type}','{difficulty}','{number_of_sets}','{set_reps}','{exercises}','{descansos}')
        ;""")

def save_plan(email, planId):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
        SELECT plansId FROM users
        WHERE email = '{email}';            
        """)
        plans = cur.fetchall()[0][0]
        if(plans != None and plans != 'null'):
            plans = json.loads(plans)
            if(planId not in plans):
                plans.append(planId)
        else:
            plans = []
            plans.append(planId)

        cur.execute(f"""
        UPDATE users
        SET plansId = '{json.dumps(plans)}'
        WHERE email = '{email}';
        """)

def get_saved_plans(email):
    list_of_plans = []
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(f"""
        SELECT plansId FROM users
        WHERE email = '{email}';
        """)
        plans = cur.fetchall()[0][0]
        if(plans != None and plans != 'null'):
            plans = json.loads(plans)
            for planId in plans:
                cur.execute(f"""
                SELECT * FROM plans
                WHERE id = '{planId}';            
                """)
                plan = cur.fetchall()[0]
                list_of_plans.append(plan)

            for i in range(len(list_of_plans)):
                list_of_plans[i] = list(list_of_plans[i])
                list_of_plans[i][6] = json.loads(list_of_plans[i][6]) # Turn ListString to List
                list_of_plans[i][7] = json.loads(list_of_plans[i][7])
                list_of_plans[i][8] = json.loads(list_of_plans[i][8])                

    return list_of_plans