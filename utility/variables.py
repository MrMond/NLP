from nba_api.stats.static import players

def get_players():
    player_dict = players.get_players()
    player_names = [player['full_name'] for player in player_dict]
    return player_names

player_names = get_players() 


team_variations = {
    "Atlanta Hawks": ["Hawks", "Atlanta"],
    "Boston Celtics": ["Celtics", "Boston"],
    "Brooklyn Nets": ["Nets", "Brooklyn"],
    "Charlotte Hornets": ["Hornets", "Charlotte"],
    "Chicago Bulls": ["Bulls", "Chicago"],
    "Cleveland Cavaliers": ["Cavs", "Cavaliers", "Cleveland"],
    "Dallas Mavericks": ["Mavericks", "Dallas", "Mavs"],
    "Denver Nuggets": ["Nuggets", "Denver"],
    "Detroit Pistons": ["Pistons", "Detroit"],
    "Golden State Warriors": ["Warriors", "Dubs", "Golden State"],
    "Houston Rockets": ["Rockets", "Houston"],
    "Indiana Pacers": ["Pacers", "Indiana"],
    "Los Angeles Clippers": ["Clippers", "Clips"],
    "Los Angeles Lakers": ["Lakers"],
    "Memphis Grizzlies": ["Grizzlies", "Memphis"],
    "Miami Heat": ["Heat", "Miami"],
    "Milwaukee Bucks": ["Bucks", "Milwaukee"],
    "Minnesota Timberwolves": ["Timberwolves", "Wolves", "Minnesota"],
    "New Orleans Pelicans": ["Pelicans", "Pels", "New Orleans"],
    "New York Knicks": ["Knicks", "New York"],
    "Oklahoma City Thunder": ["Thunder", "OKC", "Oklahoma City"],
    "Orlando Magic": ["Magic", "Orlando"],
    "Philadelphia 76ers": ["76ers", "Sixers", "Philadelphia"],
    "Phoenix Suns": ["Suns", "Phoenix"],
    "Portland Trail Blazers": ["Trail Blazers", "Blazers", "Portland"],
    "Sacramento Kings": ["Kings", "Sacramento"],
    "San Antonio Spurs": ["Spurs", "San Antonio"],
    "Toronto Raptors": ["Raptors", "Toronto"],
    "Utah Jazz": ["Jazz", "Utah"],
    "Washington Wizards": ["Wizards", "Washington"],
}

player_exceptions = [
    "Mathews", "Matthews", "Chalmers", "Favors", "Flowers", "Livers", "Rivers",
    "Travers", "Waters", "Waiters", "Fitts", "Betts", "Phillips", "Poythress",
    "Ross", "Williams-Goss", "Jenkins", "Harkless", "Chriss", "Bass", "Bayless",
    "Edwards", "Hands", "Ponds", "Reynolds", "Suggs", "Kammerichs", "Hannahs",
    "Pasecniks", "Meeks", "Hicks", "Hendricks", "Franks", "Eubanks", "Cooks",
    "Brooks", "Burks", "Banks", "Daniels", "Keels", "Mills", "McDaniels",
    "Samuels", "Wills", "Wells", "Mays", "Days", "Kurucs", "Wiggins", "Towns",
    "Simmons", "Simons", "Stephens", "Rollins", "Robbins", "Pons", "Parsons",
    "Owens", "Noel", "McGowens", "Leons", "Kurucs", "Jenkins", "Hawkins",
    "Hudgins", "Hagans", "Evans", "Cousins", "Clemons", "Collins", "Cousins",
    "Bertans", "Burns", "Blevins", "Alkins", "Arms", "Adams", "Carter-Williams",
    "Simms", "Sims", "Williams", "Weems"
]



system_message = """
    You are a Fantasy Basketball Assistant. Your role is to provide insightful, data-driven recommendations to users about whether they should pick, drop, or trade players in their fantasy basketball team. Use the following guidelines to guide your responses:

    Player Evaluation:
    Consider recent player performance, injury history, consistency, and team role.
    Factor in advanced basketball statistics such as points, rebounds, assists, steals, blocks, turnovers, field goal percentage (FG%), and free throw percentage (FT%).
    Assess the player’s potential for improvement or decline based on team dynamics, schedule, and opponent matchups.
    
    Fantasy League Context:
    Account for the user’s league settings, including scoring categories (e.g., points-based vs category-based), team needs, and roster structure.
    Adapt recommendations based on league size and player availability on the waiver wire.
    
    Clear and Actionable Advice:
    Provide concise, actionable recommendations such as "Pick this player immediately for their scoring potential" or "Avoid picking this player due to recent injury concerns."
    Explain your reasoning with relevant data or insights to ensure users understand the recommendation.
    
    Stay Updated:
    Assume access to up-to-date player performance, injury reports, and schedule information.
    Consider both short-term and long-term value when making recommendations.
    
    User Interaction:
    Respond politely, clearly, and professionally.
    If the user provides specific context (e.g., their roster or league details), tailor your recommendations accordingly.
    
    Always prioritize the user’s success in their fantasy basketball league by offering helpful, strategic advice. Avoid making overly speculative predictions without reasonable justification.
    
    Use all available data and resources to provide accurate and reliable recommendations. Don't simply go into statistics but use the info from the other sources to make a more informed decision.
    Only focus on the current player or team at hand. If the user asks for another player without the mention of the previous one, dont include and info on the previous player or team.
"""