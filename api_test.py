from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playergamelog, teamdetails, commonteamroster


def get_players():
    player_dict = players.get_players()
    player_names = [player['full_name'] for player in player_dict]
    return player_names

print(get_players())