from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys
sys.path.append('/mnt/c/Users/victo/OneDrive/Desktop/fantasy_nba_dashboard/db')

import insert_gamelog_today

default_args = {
    'owner': 'victor',
    'retries': 5}

with DAG(
    default_args=default_args,
    dag_id='fantasy_nba_daily_game_extract',
    description='Extract daily gamelogs and inserts into postgresql',
    start_date=datetime(2024, 1, 6),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable=insert_gamelog_today.test
        
    )
    
    task1