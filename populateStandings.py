from sqlmodel import Session
from models import standings, engine
import pandas as pd

def generate_standings_instances():
    data = pd.read_csv('standings.csv')
    standings_instances = []
    for index, row in data.iterrows():
        standings_instance = standings(
            Team=row['NFL Team'],
            W=row['W'],
            L=row['L'],
            T=row['T'],
            PCT=row['PCT'],
            PF=row['PF'],
            PA=row['PA'],
            Net_Pts=row['Net Pts'],
            Home=row['Home'],
            Away=row['Road'],
            Div=row['Div'],
            Div_Pct=row['Div_Pct'],
            Conf=row['Conf'],
            Conf_Pct=row['Conf_Pct'],
            Non_Conf=row['Non-Conf']
        )
        standings_instances.append(standings_instance)
    return standings_instances

with Session(engine) as session:
    standings_instances = generate_standings_instances()
    session.add_all(standings_instances)
    session.commit()
