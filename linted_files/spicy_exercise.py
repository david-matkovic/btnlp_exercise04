"""Module for processing text with spaCy and visualizing dependency parse."""

import spacy
from spacy import displacy

# Load the spaCy small English model
nlp = spacy.load("en_core_web_sm")

# Sample text split into multiple lines for readability
TEXT = (
    "That night, in the mid-watch, when the old man—as his wont at intervals—"
    "stepped forth from the scuttle in which he leaned, and went to his pivot-hole, "
    "he suddenly thrust out his face fiercely, snuffing up the sea air as a sagacious "
    "ship’s dog will, in drawing nigh to some barbarous isle. He declared that a whale "
    "must be near. Soon that peculiar odor, sometimes to a great distance given forth "
    "by the living sperm whale, was palpable to all the watch; nor was any mariner "
    "surprised when, after inspecting the compass, and then the dog-vane, and then "
    "ascertaining the precise bearing of the odor as nearly as possible, Ahab rapidly "
    "ordered the ship’s course to be slightly altered, and the sail to be shortened."
)

# Process the text with spaCy
doc = nlp(TEXT)

# Extract tokens and lemmas, excluding stopwords
tokens = [token.text for token in doc if not token.is_stop]
lemmas = [token.lemma_ for token in doc if not token.is_stop]
pos_tags = [(token.text, token.pos_) for token in doc]

# Visualize the dependency parse
displacy.serve(doc, style="dep")
