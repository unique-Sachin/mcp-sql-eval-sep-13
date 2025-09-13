# schema for cricket analytics database
from sqlalchemy import Table, MetaData
from model import Player, Match, Performance
from db import engine
metadata = MetaData()

players_table = Table('players', metadata, autoload_with=engine)
matches_table = Table('matches', metadata, autoload_with=engine)
performances_table = Table('performances', metadata, autoload_with=engine)