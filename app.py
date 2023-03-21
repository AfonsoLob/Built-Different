from website import create_app
from flask import render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = create_app() # create_app() in __init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)