from schema import players_table, matches_table, performances_table
from model import Player, Match, Performance
from db import get_db, engine
from sqlalchemy.orm import Session as SessionType

from typing import List, Dict

get_db_gen = get_db()
session = next(get_db_gen)

# query_player_stats: Player performance analytics
def query_player_stats(session: SessionType, player_id: int) -> List[Dict]:
    result = session.execute(
        performances_table.select().where(performances_table.c.player_id == player_id)
    ).fetchall()
    return [row._asdict() for row in result]

# match_analysis: Match-level insights and comparisons
def match_analysis(session: SessionType, match_id: int) -> List[Dict]:
    result = session.execute(
        performances_table.select().where(performances_table.c.match_id == match_id)
    ).fetchall()
    return [row._asdict() for row in result]

# team_performance: Team statistics and trends
def team_performance(session: SessionType, team_name: str) -> List[Dict]:
    result = session.execute(
        performances_table.select().where(performances_table.c.team == team_name)
    ).fetchall()
    return [row._asdict() for row in result]

# season_comparisons: Cross-season analysis
def season_comparisons(session: SessionType, player_id: int) -> List[Dict]:
    result = session.execute(
        performances_table.select().where(performances_table.c.player_id == player_id)
    ).fetchall()
    return [row._asdict() for row in result]

# head_to_head: Team vs team historical data
def head_to_head(session: SessionType, team1: str, team2: str) -> List[Dict]:
    result = session.execute(
        performances_table.select().where(
            (performances_table.c.team == team1) | (performances_table.c.team == team2)
        )
    ).fetchall()
    return [row._asdict() for row in result]

# create sample data

def create_sample_data(session: SessionType):
    # add players
    players = [
        Player(name="Sachin Tendulkar", age=47, team="India"),
        Player(name="Brian Lara", age=50, team="West Indies"),
        Player(name="Muttiah Muralitharan", age=48, team="Sri Lanka"),
        Player(name="Ricky Ponting", age=45, team="Australia"),
        Player(name="Andrew Flintoff", age=44, team="England"),
        Player(name="Virat Kohli", age=34, team="India"),
        Player(name="Steve Smith", age=32, team="Australia"),
        Player(name="Joe Root", age=31, team="England"),
        Player(name="Chris Gayle", age=42, team="West Indies"),
        Player(name="Kumar Sangakkara", age=43, team="Sri Lanka"),
    ]
    session.add_all(players)
    session.commit()

    # add matches
    matches = [
        Match(date="2023-01-01", venue="Mumbai", team1="India", team2="Australia", winner="India"),
        Match(date="2023-02-15", venue="Sydney", team1="Australia", team2="England", winner="England"),
        Match(date="2023-03-10", venue="Colombo", team1="Sri Lanka", team2="India", winner="Sri Lanka"),
        Match(date="2023-04-05", venue="London", team1="England", team2="West Indies", winner="West Indies"),
        Match(date="2023-05-20", venue="Kingston", team1="West Indies", team2="Sri Lanka", winner="West Indies"),
        Match(date="2023-06-15", venue="Delhi", team1="India", team2="West Indies", winner="India"),
        Match(date="2023-07-30", venue="Melbourne", team1="Australia", team2="Sri Lanka", winner="Australia"),
        Match(date="2023-08-25", venue="Birmingham", team1="England", team2="India", winner="India"),
        Match(date="2023-09-10", venue="Perth", team1="Australia", team2="West Indies", winner="Australia"),
        Match(date="2023-10-05", venue="Kandy", team1="Sri Lanka", team2="England", winner="Sri Lanka"),
    ]
    session.add_all(matches)
    session.commit()

    # add performances
    performances = [
        Performance(player_id=1, match_id=1, runs=100, wickets=0, catches=1, team="India"),
        Performance(player_id=2, match_id=1, runs=80, wickets=0, catches=0, team="India"),
        Performance(player_id=3, match_id=2, runs=10, wickets=5, catches=0, team="Sri Lanka"),
        Performance(player_id=4, match_id=2, runs=90, wickets=0, catches=1, team="Australia"),
        Performance(player_id=5, match_id=3, runs=70, wickets=2, catches=0, team="England"),
        Performance(player_id=6, match_id=3, runs=110, wickets=0, catches=1, team="India"),
        Performance(player_id=7, match_id=4, runs=95, wickets=0, catches=2, team="Australia"),
        Performance(player_id=8, match_id=4, runs=85, wickets=1, catches=0, team="England"),
        Performance(player_id=9, match_id=5, runs=120, wickets=0, catches=1, team="West Indies"),
        Performance(player_id=10, match_id=5, runs=60, wickets=3, catches=0, team="Sri Lanka"),
    ]
    session.add_all(performances)
    session.commit()

# Example usage
if __name__ == "__main__":
    print("Player 1 Stats:", query_player_stats(session, 1))
    print("Match 1 Analysis:", match_analysis(session, 1))
    print("Team India Performance:", team_performance(session, "India"))
    print("Season Comparisons for Player 1:", season_comparisons(session, 1))
    print("Head to Head India vs Australia:", head_to_head(session, "India", "Australia"))
    # session.close()