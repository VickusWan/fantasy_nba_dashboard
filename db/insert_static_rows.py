from create_tables import teams, players, draft_salaries, roster, player_gamelog
from insert_rows import insert_row
from nba_api.stats.static import teams
import pandas as pd

nba_teams = teams.get_teams()
for team in nba_teams:
    insert_row(
    teams,
    id=team['id'],
    full_name=team['full_name'],
    abbreviation=team['abbreviation'],
    nickname=team['nickname'],
    city=team['city'],
    state=team['state'],
    year_founded=team['year_founded'])

nba_players = players.get_players()
for player in nba_players:
    insert_row(
    players,
    id=player['id'],
    full_name=player['full_name'],
    first_name=player['first_name'],
    last_name=player['last_name'],
    is_active=player['is_active']
    )
    

df = pd.read_csv('db/draft_salary.csv')
for key, values in df.to_dict(orient='index').items():
    print(values)
    insert_row(draft_salaries,
    rank = values['Rank'],
    player_name = values['PLAYER'],
    position = values['POS'],
    team = values['TEAM'],
    salary = values['TOTAL'])