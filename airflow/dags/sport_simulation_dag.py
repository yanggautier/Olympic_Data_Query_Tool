from pendulum import datetime
from datetime import timedelta
import os
from airflow.sdk import dag, task
from utils.simulation_data import generate_sports
from sqlalchemy import create_engine


@dag(
    start_date=datetime(2025, 6, 8),
    schedule=timedelta(minutes=2),
    end_date=datetime(2026, 6, 9),
    catchup=False,
    tags=["sport", "olympic", "data"]
)
def olympic_data_generation():
    @task()
    def get_generate_data():
        df = generate_sports(context={"logical_date": 1988})
        return df

    @task()
    def load(df):
        connect_string = os.getenv("DB_CONNECT_STRING")
        if connect_string:
            engine = create_engine(connect_string)
            df.to_sql(
                name='resultats_olympiques',
                con=engine,
                schema='olympic',
                if_exists='append',
                index=False)
        else:
            raise Exception("Impossibe de connecter à la base de données")

    data = get_generate_data()
    load(data)


olympic_data_generation()
