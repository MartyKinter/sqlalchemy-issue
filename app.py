from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///pet_shop_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def home_page():
    return render_template('home.html')