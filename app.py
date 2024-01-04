from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import pandas as pd
from db.create_tables import db, teams, players, draft_salaries, roster, player_gamelog

load_dotenv()
database_url = os.getenv("DATABASE_URL")
print("Database URL:", database_url)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()