
import os
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data_path = r"C:\Users\dama010\Documents\Miscellanea\All things Python\Neuer Ordner\btnlp_exercise03\archive"


def preprocess_text(content):
    # Adjust these patterns to match the actual headers, footers, and quotes in your files
    content = re.sub(r'Header:.*\n', '', content)
    content = re.sub(r'Footer:.*\n', '', content)
    content = re.sub(r'^>.*\n?', '', content, flags=re.MULTILINE)
    return content


data = []
labels = []
for filename in os.listdir(data_path):
    file_path = os.path.join(data_path, filename)
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        content_cleaned = preprocess_text(content)
        data.append(content_cleaned)
        # Assuming the label is the whole filename without the extension
        labels.append(filename.rsplit('.', 1)[0])

# Print out the labels to verify they are extracted correctly
print("Labels:", np.unique(labels))

# Encode the labels to integers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(labels)

# Convert the text data to numerical data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.3, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


f1 = f1_score(y_test, y_pred, average='weighted')
print(f"F1 Score: {f1}")


print("\nSample preprocessed text:")
for sample in data[:3]:  # print first 3 samples
    print(sample[:500])  # print first 500 characters of each sample
