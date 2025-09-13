# create cricket analytics models using SQLAlchemy
from tkinter.messagebox import IGNORE
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from db import engine

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    team = Column(String)

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    venue = Column(String)
    team1 = Column(String)
    team2 = Column(String)
    winner = Column(String)

class Performance(Base):
    __tablename__ = 'performances'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    match_id = Column(Integer, ForeignKey('matches.id'))
    team = Column(String)
    runs = Column(Integer)
    wickets = Column(Integer)
    catches = Column(Integer)

# create tables if not exist
Player.__table__.create(bind=engine, checkfirst=True) 
Match.__table__.create(bind=engine, checkfirst=True)
Performance.__table__.create(bind=engine, checkfirst=True)