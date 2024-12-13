import spacy
from spacy.matcher import Matcher
from variables import team_variations
from helper_functions import remove_possessive, matcher, fuzzy_matcher


class EntityExtractor:
    """
    A class to extract player names and NBA team names from text using SpaCy and custom matchers.
    """

    def __init__(self, model="en_core_web_lg", team_variations=team_variations, fuzzy_threshold=80):
        """
        Initialize the EntityExtractor with a SpaCy model and optional list of NBA teams.
        """
        self.nlp = spacy.load(model)
        self.matcher = Matcher(self.nlp.vocab)

        # Default NBA teams if not provided
        self.team_variations = team_variations

        # Create a reverse lookup dictionary for team variations
        self.reverse_team_lookup = {
            variation: key
            for key, variations in self.team_variations.items()
            for variation in variations
        }

        # Add team name patterns to the matcher
        self._add_team_patterns()

        # Fuzzy matching threshold
        self.fuzzy_threshold = fuzzy_threshold

    def _add_team_patterns(self):
        """Add NBA team patterns to the matcher."""
        patterns = [[{"LOWER": variation.lower(
        )}] for variations in self.team_variations.values() for variation in variations]
        self.matcher.add("NBA_TEAMS", patterns)

    def extract_entities(self, text):
        """
        Extract player names and team names from the given text.

        Args:
            text (str): Input text.

        Returns:
            dict: Dictionary containing extracted player and team names.
        """
        doc = self.nlp(text.title())
        entities = {"player_names": [], "team_names": []}

        # Named Entity Recognition for players
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities["player_names"].append(ent.text)

        # Custom rules for removing possessives from player names
        entities["player_names"] = remove_possessive(entities["player_names"])

        # Custom matcher for team names (including variations)
        matches = self.matcher(doc)
        entities = matcher(self, matches, doc, entities)

        # Fuzzy matching for team names if no exact matches found
        if not entities["team_names"]:
            entities = fuzzy_matcher(self, doc, entities)

        # Deduplicate team names
        entities["team_names"] = list(set(entities["team_names"]))
        return entities


# Testing Area
# Initialize the extractor
extractor = EntityExtractor()

# Test Input
text_1 = "How would you judge lebron james performance?"
text_2 = "How would you judge anthony edwards performance?"
text_3 = "What players from the Indian are peforming well??"

# Extract Entities
result_1 = extractor.extract_entities(text_1)
result_2 = extractor.extract_entities(text_2)
result_3 = extractor.extract_entities(text_3)

print("Result 1:", result_1)
print("Result 2:", result_2)
print("Result 3:", result_3)