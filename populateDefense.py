from sqlmodel import Session
from models import defense, engine
import pandas as pd

def generate_defense_instances():
    data = pd.read_csv('defense.csv')
    defense_instances = []
    for index, row in data.iterrows():
        defense_instance = defense(
            Team=row['TEAMS'],
            GP=row['GP'],
            PA=row['PA'],
            PA_G=row['PA/G'],
            YDS_G=row['YDS/G'],
            PYDS=row['PYDS'],
            PYDS_G=row['PYDS/G'],
            RYDS=row['RYDS'],
            RYDS_G=row['RYDS/G'],
            SCK=row['SCK'],
            SCK_YDS=row['SCK YDS'],
            DEF_INT=row['DEF INT'],
            INTTD=row['INTTD'],
            FF=row['FF'],
            FUMR=row['FUMR'],
            FUMTD=row['FUMTD'],
            HUR=row['HUR'],
            PDEF=row['PDEF'],
            SFTY=row['SFTY']
        )
        defense_instances.append(defense_instance)
    return defense_instances

with Session(engine) as session:
    defense_instances = generate_defense_instances()
    session.add_all(defense_instances)
    session.commit()

