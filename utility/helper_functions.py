from utility.variables import player_exceptions
from fuzzywuzzy import process

# Function to handle possessive forms in player names


def remove_possessive(player_list):
    """
    Removes possessive forms (e.g., "Player's", "Players'") and adjusts names
    that end with 's' based on specific rules.

    Args:
        player_list (list): List of player names.

    Returns:
        list: Updated list of player names with possessive forms handled.
    """
    for player in player_list:
        modified_player = player
        # Handle names ending with "'s" (e.g., "Jordan's")
        if player.endswith("'s"):
            modified_player = player[:-2]  # Remove possessive 's
        # Handle names ending with "s'" (e.g., "Wiggins'")
        elif player.endswith("s'"):
            modified_player = player[:-1]  # Remove possessive apostrophe
        # Remove the final 's' if not in exceptions and it's a consonant ending
        elif (
            player.split()[-1] not in player_exceptions
            and player.endswith("s")
            and player[-2].lower() not in "aeiou"
        ):
            modified_player = player[:-1]

        # If the name was modified, update the list
        if modified_player != player:
            player_list.remove(player)
            player_list.append(modified_player)

    return player_list

# Function to match and map team names using pre-defined rules


def matcher(self, matches, doc, entities):
    """
    Matches identified spans in the document against a reverse lookup table
    and updates the list of team names in the entities dictionary.

    Args:
        self: The object instance containing `reverse_team_lookup`.
        matches (list): List of matches (tuples) containing match_id, start, and end indices.
        doc: The processed document object (e.g., from spaCy).
        entities (dict): Dictionary to store extracted entity information.

    Returns:
        dict: Updated entities dictionary with team names.
    """
    for match_id, start, end in matches:
        # Extract the matched text span
        team_name = doc[start:end].text
        # Map the matched team name using reverse lookup or fallback to the original name
        team_key = self.reverse_team_lookup.get(team_name, team_name)
        # Add the team name to the entities if not already present
        if team_key not in entities["team_names"]:
            entities["team_names"].append(team_key)

    return entities

# Function to perform fuzzy matching for team names


def fuzzy_matcher(self, doc, entities):
    """
    Performs fuzzy matching to identify team names in the document and updates
    the list of team names in the entities dictionary.

    Args:
        self: The object instance containing `reverse_team_lookup` and `fuzzy_threshold`.
        doc: The processed document object (e.g., from spaCy).
        entities (dict): Dictionary to store extracted entity information.

    Returns:
        dict: Updated entities dictionary with team names.
    """
    # List of team names for matching
    team_list = list(self.reverse_team_lookup.keys())
    for token in doc:
        # Perform fuzzy matching for the token text
        fuzzy_match, score = process.extractOne(token.text, team_list)
        # Check if the match score meets the threshold
        if score >= self.fuzzy_threshold:
            # Map the fuzzy-matched name using reverse lookup or fallback to the matched name
            team_key = self.reverse_team_lookup.get(fuzzy_match, fuzzy_match)
            # Add the team name to the entities if not already present
            if team_key not in entities["team_names"]:
                entities["team_names"].append(team_key)

    return entities
