from flask_sqlalchemy import SQLAlchemy
import sys
import os

# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, parent_dir)
# from app import app

db = SQLAlchemy()

class teams(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    abbreviation = db.Column(db.String(4), nullable=False)
    nickname = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    year_founded = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<teams {self.name}>'

class players(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<players {self.name}>'

class draft_salaries(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255), nullable=False)
    team = db.Column(db.String(4), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<draft_salaries {self.name}>'
    
class roster(db.Model):
    team_id = db.Column(db.String(255), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    league_id = db.Column(db.String(255), nullable=False)
    player_name = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(255), nullable=False)
    player_slug = db.Column(db.String(255), nullable=False)
    jersey_num = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(255), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.String(255), primary_key=True)
    how_acquired = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<roster {self.name}>'

class player_gamelog(db.Model):
    
    season_id = db.Column(db.String(255), nullable=False)
    player_id = db.Column(db.String(255), nullable=False)
    game_id = db.Column(db.String(255), primary_key=True)
    game_date = db.Column(db.String(255), nullable=False)
    matchup = db.Column(db.String(255), nullable=False)
    win_loss = db.Column(db.String(5), nullable=False)
    minutes = db.Column(db.Integer, nullable=False)
    
    fgm = db.Column(db.Integer, nullable=False)
    fga = db.Column(db.Integer, nullable=False)
    fg_pct = db.Column(db.Float, nullable=False)
    
    fg3m = db.Column(db.Integer, nullable=False)
    fg3a = db.Column(db.Integer, nullable=False)
    fg3_pct = db.Column(db.Float, nullable=False)
    
    ftm = db.Column(db.Integer, nullable=False)
    fta = db.Column(db.Integer, nullable=False)
    ft_pct = db.Column(db.Float, nullable=False)
    
    oreb = db.Column(db.Integer, nullable=False)
    dreb = db.Column(db.Integer, nullable=False)
    reb = db.Column(db.Integer, nullable=False)
    
    ast = db.Column(db.Integer, nullable=False)
    stl = db.Column(db.Integer, nullable=False)
    blk = db.Column(db.Integer, nullable=False)
    tov = db.Column(db.Integer, nullable=False)
    pf = db.Column(db.Integer, nullable=False)
    
    pts = db.Column(db.Integer, nullable=False)
    plus_minus = db.Column(db.Integer, nullable=False)
    video_available = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<player_gamelog {self.name}>'

