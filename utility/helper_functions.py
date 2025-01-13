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
        modified_player = player.title()
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
        team_key = self.reverse_team_lookup.get(team_name.title(), team_name)
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

    # Iterate through tokens and multi-token spans
    for span in doc:
        # Skip stop-words and non-proper nouns
        if span.is_stop or span.pos_ not in {"PROPN", "NOUN"}:
            continue

        # Perform fuzzy matching for the token text
        fuzzy_match, score = process.extractOne(span.text, team_list)

        # Check if the match score meets the threshold
        # Adjust threshold for single-token matches
        if len(span.text.split()) == 1 and score < self.fuzzy_threshold + 10:
            continue

        if score >= self.fuzzy_threshold:
            # Map the fuzzy-matched name using reverse lookup or fallback to the matched name
            team_key = self.reverse_team_lookup.get(fuzzy_match, fuzzy_match)

            # Add the team name to the entities if not already present
            if team_key not in entities["team_names"]:
                entities["team_names"].append(team_key)

    return entities

def fuzzy_matcher_for_players(self, entities, player_list):
    """
    Performs fuzzy matching to identify and correct player names in the entities dictionary.

    Args:
        entities (dict): Dictionary containing extracted entity information, including `player_names`.
        player_list (list): List of valid player names for matching.
        fuzzy_threshold (int): Threshold for fuzzy matching (default is 90).

    Returns:
        dict: Updated entities dictionary with corrected player names.
    """
    # Ensure "player_names" exists in the entities dictionary
    if "player_names" not in entities:
        entities["player_names"] = []

    corrected_player_names = []

    # Iterate through player names in the entities
    for name in entities["player_names"]:
        # Perform fuzzy matching to find the closest player name
        fuzzy_match, score = process.extractOne(name, player_list)

        # Check if the match score meets the threshold
        if score >= self.fuzzy_threshold:
            # Use the fuzzy-matched name as the corrected name
            corrected_player_names.append(fuzzy_match)
        else:
            # If no good match is found, keep the original name
            corrected_player_names.append(name)

    # Update the "player_names" key in the entities dictionary
    entities["player_names"] = corrected_player_names

    return entities
