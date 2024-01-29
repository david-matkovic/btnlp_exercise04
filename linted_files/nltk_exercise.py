import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk import pos_tag

# Ensure you have the required NLTK resources downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Text from Moby Dick Chapter 133
text = """That night, in the mid-watch, when the old man—as his wont at intervals—stepped forth from the scuttle in which he leaned, and went to his pivot-hole, he suddenly
        thrust out his face fiercely, snuffing up the sea air as a sagacious ship’s dog will, in
        drawing nigh to some barbarous isle. He declared that a whale must be near. Soon that
        peculiar odor, sometimes to a great distance given forth by the living sperm whale,
        was palpable to all the watch; nor was any mariner surprised when, after inspecting
        the compass, and then the dog-vane, and then ascertaining the precise bearing of the
        odor as nearly as possible, Ahab rapidly ordered the ship’s course to be slightly altered,
        and the sail to be shortened."""

# Tokenization and preprocessing
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if not w.lower() in stop_words]
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]
pos_tags = pos_tag(filtered_tokens)


grammar = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)

first_sentence = sent_tokenize(text)[0]
first_sentence_tokens = word_tokenize(first_sentence)

first_sentence_pos_tags = pos_tag(first_sentence_tokens)

tree = cp.parse(first_sentence_pos_tags)

tree.draw()
