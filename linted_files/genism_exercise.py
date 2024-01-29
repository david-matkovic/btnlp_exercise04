"""Module for preprocessing text and creating a bag of words model using Gensim."""

from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora

# Sample text
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


def preprocess_text(text):
    """Tokenize text and remove stopwords."""
    tokens = simple_preprocess(text)
    return [word for word in tokens if word not in STOPWORDS]


def create_bow_model(tokens):
    """Create a bag of words model."""
    dictionary = corpora.Dictionary([tokens])
    return [dictionary.doc2bow(doc) for doc in [tokens]]


filtered_tokens = preprocess_text(TEXT)
bow_corpus = create_bow_model(filtered_tokens)

print("Tokenized Text:", simple_preprocess(TEXT))
print("Filtered Tokens:", filtered_tokens)
print("Bag of Words Model:", bow_corpus)
