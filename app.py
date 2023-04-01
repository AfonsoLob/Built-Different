from website import create_app
from flask import render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = create_app() # create_app() in __init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = b'*51_.2S7H2F\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)



if __name__ == "__main__":
    app.run(debug=True)