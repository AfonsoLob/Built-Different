import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

DB_STRING = "database.db"

db_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(db_directory, DB_STRING)

def setup_database():
    user_table = """ CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        username TEXT NOT NULL
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

def cleanup_database():
    users_table = "DROP TABLE IF EXISTS user_stats;"
    with sqlite3.connect(db_path) as con:
        con.execute(users_table)

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
        

def create_user_stats(email):
    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        INSERT INTO user_stats (email, age, height, weight)
        VALUES ('{email}', '#', '#' , '#');
        """)

def update_stats(email, age, height, weight):
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