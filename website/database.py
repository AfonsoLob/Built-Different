import sqlite3
import os

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

def cleanup_database():
    users_table = "DROP TABLE IF EXISTS users;"
    with sqlite3.connect(db_path) as con:
        con.execute(users_table)

def verify_user(user_email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
            SELECT email from users;
        """)
        list_of_emails = cur.fetchall()
        for email in list_of_emails:
            email = email[0]
            if (email == user_email): 
                return False
        return True
    
def add_user(email, password, username):
    with sqlite3.connect(db_path) as con:
        con.execute(f"""
        INSERT INTO users (email, password, username)
        VALUES ('{email}','{password}','{username}');
        """)