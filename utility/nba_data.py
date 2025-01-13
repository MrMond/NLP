from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playergamelog, teamdetails, commonteamroster
from unidecode import unidecode
import json

def normalize_name(name):
    """
    Normalize names by removing special characters.
    """
    return unidecode(name.lower())

def find_player_by_name(player_name):
    """
    Find player ID by name, normalizing names to handle special characters.
    """
    player_dict = players.get_players()
    normalized_input = normalize_name(player_name)

    # Search for the player
    matching_players = [
        player for player in player_dict 
        if normalize_name(player['full_name']) == normalized_input
    ]

    return matching_players[0] if matching_players else None

def find_team_by_name(team_name):
    """
    Find team ID by name, normalizing names to handle special characters.
    """
    team_dict = teams.get_teams()
    normalized_input = normalize_name(team_name)

    # Search for the team
    matching_teams = [
        team for team in team_dict 
        if normalize_name(team['full_name']) == normalized_input
    ]

    return matching_teams[0] if matching_teams else None

def get_recent_performance(player_id):
    """
    Retrieve recent game performance for a player.
    """
    game_logs = playergamelog.PlayerGameLog(player_id=player_id, season_type_all_star="Regular Season").get_normalized_dict()
    recent_games = game_logs.get('PlayerGameLog', [])

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
    # Find player by name
    player = find_player_by_name(player_name)
    if not player:
        return {'Error': f"Player '{player_name}' not found."}

    player_id = player['id']

    # Fetch player info
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()

    # Fetch recent game logs
    recent_performance = get_recent_performance(player_id=player_id)

    return {
        'Name': player['full_name'],
        'RecentGames': recent_performance,
        'SeasonStats': player_info['PlayerHeadlineStats'][0] if player_info.get('PlayerHeadlineStats') else "No stats available",
    }

def get_team_info(team_name):
    """
    Retrieve detailed team information and its players' recent performances using nba_api.
    """
    # Find team by name
    team = find_team_by_name(team_name)
    if not team:
        return {'Error': f"Team '{team_name}' not found."}

    team_id = team['id']

    # Fetch team details
    team_info = teamdetails.TeamDetails(team_id=team_id).get_normalized_dict()

    # Fetch team roster
    roster_info = commonteamroster.CommonTeamRoster(team_id=team_id).get_normalized_dict()
    players_on_team = roster_info.get('CommonTeamRoster', [])

    # Fetch recent performance for all players
    team_players = {
        player['PLAYER']: get_recent_performance(player_id=player['PLAYER_ID'])
        for player in players_on_team
    }

    return {
        'Team Name': team['full_name'],
        'Players': team_players
    }

def fetch_context(input_dict):
    """
    Fetches relevant statistics for LLM from the provided player and team names.

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