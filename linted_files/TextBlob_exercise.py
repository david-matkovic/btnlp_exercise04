"""Module for text analysis using TextBlob."""

from textblob import TextBlob

TEXT = (
    "That night, in the mid-watch, when the old man—as his wont at intervals—stepped "
    "forth from the scuttle in which he leaned, and went to his pivot-hole, he suddenly "
    "thrust out his face fiercely, snuffing up the sea air as a sagacious ship’s dog will, in "
    "drawing nigh to some barbarous isle. He declared that a whale must be near. Soon that "
    "peculiar odor, sometimes to a great distance given forth by the living sperm whale, "
    "was palpable to all the watch; nor was any mariner surprised when, after inspecting "
    "the compass, and then the dog-vane, and then ascertaining the precise bearing of the "
    "odor as nearly as possible, Ahab rapidly ordered the ship’s course to be slightly altered, "
    "and the sail to be shortened."
)

blob = TextBlob(TEXT)

tokens = blob.words
pos_tags = blob.tags
sentiment = blob.sentiment

print("Tokenized Text:", tokens)
print("Parts of Speech Tags:", pos_tags)
print("Sentiment of the text:", sentiment)
