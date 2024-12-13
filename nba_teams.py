from nba_api.stats.static import teams

# Get all NBA teams
nba_teams = teams.get_teams()

# Display each team's metadata
for team in nba_teams:
    print(team["full_name"])
