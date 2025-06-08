import pandas as pd
import os
import random


def generate_date(year):
    random_year = random.randint(year+1, year + 4)
    month = random.randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif random_year % 4 == 0:
        day = random.randint(1, 29)
    else:
        day = random.randint(1, 28)
    return f"{day}/{month}/{random_year}"


def generate_sports(**context):
    """
    Function generate Olympic game data
    :return:
    """
    if "logical_date" not in context:
        logical_date = 2002
    else:
        logical_date = context["logical_date"]

    context["logical_date"] = logical_date + 4

    file_path = os.path.join(os.environ["AIRFLOW_HOME"], 'dags/data', 'fact_resultats_epreuves.csv')
    df = pd.read_csv(file_path)

    sample_nb = random.randint(800, 1200)
    random_df = df.sample(n=sample_nb)
    random_df["id_resultat"] = random_df["id_resultat"].apply(lambda x: random.randint(1, 99999999))
    random_df["id_resultat_source"] = random_df["id_resultat_source"].apply(lambda x: random.randint(1, 99999999))
    random_df["id_athlete_base_resultats"] = random_df["id_athlete_base_resultats"].apply(lambda x: random.randint(1, 99099999))
    random_df["date_debut_edition"] = random_df["date_debut_edition"].apply(lambda x: generate_date(logical_date))
    return random_df


