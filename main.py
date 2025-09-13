# use sql_agent to create a mcp server using FastMCP
from typing import List, Dict
from sqlalchemy.orm import Session as SessionType
from sql_agent import (
    query_player_stats,
    match_analysis,
    team_performance,
    season_comparisons,
    head_to_head,
)
from db import get_db
from fastmcp import FastMCP

mcp = FastMCP()

get_db_gen = get_db()
session = next(get_db_gen)

# create query_player_stats tool

@mcp.tool(
    name="player_stats_tool",
    description="Get player performance statistics by player ID.",
    tags={"player", "stats"},
    meta={"version": "1.0", "author": "sql-agent"}  
)
def player_stats_tool(player_id: int) -> List[Dict]:
    """Get player performance statistics by player ID."""
    return query_player_stats(session, player_id)

@mcp.tool(  
    name="match_analysis_tool",
    description="Get match analysis by match ID.",
    tags={"match", "analysis"},
    meta={"version": "1.0", "author": "sql-agent"}  
)
def match_analysis_tool(match_id: int) -> List[Dict]:
    """Get match analysis by match ID."""
    return match_analysis(session, match_id)

@mcp.tool(  
    name="team_performance_tool",
    description="Get team performance statistics by team name.",
    tags={"team", "performance"},
    meta={"version": "1.0", "author": "sql-agent"}
)
def team_performance_tool(team_name: str) -> List[Dict]:
    """Get team performance statistics by team name."""
    return team_performance(session, team_name)

@mcp.tool(
    name="season_comparisons_tool",
    description="Get season comparisons for a player by player ID.",
    tags={"season", "comparisons"},
    meta={"version": "1.0", "author": "sql-agent"}
)
def season_comparisons_tool(player_id: int) -> List[Dict]:
    """Get season comparisons for a player by player ID."""
    return season_comparisons(session, player_id)

@mcp.tool(
    name="head_to_head_tool",
    description="Get head-to-head statistics between two teams.",
    tags={"head", "to", "head"},
    meta={"version": "1.0", "author": "sql-agent"}
)
def head_to_head_tool(team1: str, team2: str) -> List[Dict]:
    """Get head-to-head statistics between two teams."""
    return head_to_head(session, team1, team2)

if __name__ == "__main__":
    mcp.run()