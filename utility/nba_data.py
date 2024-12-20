from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playergamelog, teamdetails, commonteamroster
import json

def get_recent_performance(player_id):
    """
    Retrieve recent game performance for a player.
    """
    game_logs = playergamelog.PlayerGameLog(player_id=player_id, season_type_all_star="Regular Season").get_normalized_dict()
    recent_games = game_logs['PlayerGameLog'] if 'PlayerGameLog' in game_logs else []

    return [
        {
            'GameDate': game['GAME_DATE'],
            'Opponent': game['MATCHUP'],
            'Points': game['PTS'],
            'Rebounds': game['REB'],
            'Assists': game['AST'],
            'Minutes': game['MIN']
        } for game in recent_games[:5]
    ]

def get_player_info(player_name):
    """
    Retrieve detailed player information and recent game performance using nba_api.
    """
    # Resolve player ID from name
    player_dict = players.find_players_by_full_name(player_name)
    if not player_dict:
        return {'Error': f"Player '{player_name}' not found."}
    
    player_id = player_dict[0]['id']
    
    # Fetch player info
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()
    
    # Fetch recent game logs
    recent_performance = get_recent_performance(player_id=player_id)

    return {
        'Name': player_name,
        'RecentGames': recent_performance,
        'SeasonStats': player_info['PlayerHeadlineStats'][0] if player_info['PlayerHeadlineStats'] else "No stats available",
    }

def get_team_info(team_name):
    """
    Retrieve detailed team information and its players' recent performances using nba_api.
    """
    # Resolve team ID from full name
    team_dict = teams.find_teams_by_full_name(team_name)
    if not team_dict:
        return {'Error': f"Team '{team_name}' not found."}
    
    team_id = team_dict[0]['id']

    # Fetch team details
    team_info = teamdetails.TeamDetails(team_id=team_id).get_normalized_dict()

    # Fetch team roster
    roster_info = commonteamroster.CommonTeamRoster(team_id=team_id).get_normalized_dict()
    players_on_team = roster_info['CommonTeamRoster'] if 'CommonTeamRoster' in roster_info else []

    # Fetch recent performance for all players
    team_players = {
        player['PLAYER']: get_recent_performance(player_id=player['PLAYER_ID'])
        for player in players_on_team
    }

    return {
        'Team Name': team_dict[0]['full_name'],
        'Players': team_players
    }


def fetch_context(input_dict):
    """
    Fetches relevant context for LLM from the provided player and team names.

    Parameters:
        input_dict (dict): Dictionary containing 'player_names' and 'team_names'.

    Returns:
        dict: Context containing information about players and teams.
    """
    player_names = input_dict.get('player_names', [])
    team_names = input_dict.get('team_names', [])

    context = {
        'Players': {},
        'Teams': {}
    }

    for player_name in player_names:
        player_info = get_player_info(player_name)
        context['Players'][player_name] = player_info

    for team_name in team_names:
        team_info = get_team_info(team_name)
        context['Teams'][team_name] = team_info

    return context

