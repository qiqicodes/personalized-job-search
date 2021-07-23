from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrets-olala'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///job-search-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# In case need to turn of redirects:
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    '''Homepage'''

    return render_template('homepage.html')

