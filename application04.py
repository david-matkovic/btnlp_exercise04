#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
# nltk.download('averaged_perceptron_tagger')
from nltk.probability import FreqDist
# nltk.download('universal_tagset')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from gensim import corpora
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


# In[2]:


pre_df = pd.read_csv('/Users/dianadavidson/Desktop/ToolsforNLP-UdS/btnlp_exercise03-attempt2/application03/twitter_training.csv')


# In[3]:


# preview dataset
pre_df.info()
print(pre_df.head(10))


# In[4]:


# fill NaN values in 'im getting on borderlands...' columns with 'No data found'
pre_df['im getting on borderlands and i will murder you all ,'] = pre_df['im getting on borderlands and i will murder you all ,'].fillna("No data found")

# make sure that .fillna() method worked
pre_df.isna().sum()


# In[5]:


# lowercase "I'm getting on borderlands" column 
pre_df['im getting on borderlands and i will murder you all ,'] = pre_df['im getting on borderlands and i will murder you all ,'].str.lower()


# In[6]:


tweet_data = list(pre_df["im getting on borderlands and i will murder you all ,"].values)
tweet_data


# In[7]:


# Remove all non-ASCII characters and fill with whitespace

removed_data = [re.sub("[\W_]+", " ", string) for string in tweet_data]    
removed_data


# In[8]:


# Remove additional whitespace

no_space_data = [string.strip() for string in removed_data]
no_space_data

# .strip() to remove any leading or trailing white space from the string.


# In[9]:


# remove stopwords from text - using NTLK
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)


# In[10]:


remove_stopwords(no_space_data[0])


# In[12]:


no_stopwords_nltk = []

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

# iterate through each row in no_space_data
for index in range(len(no_space_data)):
    # use remove_stopwords function and append to new column called no_stopwords_nltk
    no_stopwords_nltk.append(remove_stopwords(no_space_data[index]))


# In[13]:


no_stopwords_nltk


# In[ ]:


# Remove stopwords with SpaCy


# In[15]:


import spacy


# In[16]:


nlp = spacy.load('en_core_web_sm')


# In[23]:



# spacy_strings = ''.join(no_space_data)
# doc = nlp(spacy_strings)

# When I ran these two lines, I got a ValueError saying that the text length of 7645036 exceeds maximum of 1000000.
# I need to separate into chunks - HOWEVER, if doc has been cleaned first, then maybe this won't be an issue

# this code is taking forever to run

chunk_size = 100000  # specified chunk size
chunks = [no_space_data[i:i + chunk_size] for i in range(0, len(no_space_data), chunk_size)]

processed_docs = []

for chunk in chunks:
    text = ' '.join(chunk)
    doc = nlp(text)
    processed_docs.append(doc)


# In[ ]:


stopwords = nlp.Defaults.stop_words


# In[ ]:


no_stopwords_moby = []

for token in doc:
    lowercase_text = token.text.lower()
    # check if a word in lowercase is not in stopwords list from spaCy
    if lowercase_text not in stopwords:
        no_stopwords_moby.append(token.text)
        

# no_stopwords_text = ' '.join(no_stopwords_moby)
no_stopwords_doc = nlp(' '.join(no_stopwords_moby))
print(no_stopwords_doc)


# In[ ]:


# Remove stopwords with Gensim


# In[35]:


from gensim.utils import simple_preprocess


# In[38]:


no_stopwords_gensim = []

# Tokenize data and remove stopwords
for text in no_space_data:
    tokens = remove_stopword_tokens(simple_preprocess(text))
    no_stopwords_gensim.append(tokens)

# Checkt that it worked
for tokens in no_stopwords_gensim:
    print(tokens)


# In[ ]:


# Remove stopwords with Textblob


# In[39]:


from textblob import TextBlob


# In[53]:


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

no_stopwords_textblob = []

# Apply remove_stopwords function and append to the new list
for sentences in no_space_data:
    filtered_text = remove_stopwords(' '.join(sentences))
    no_stopwords_textblob.append(filtered_text)

textblob_object = TextBlob(' '.join(no_stopwords_textblob))
print(textblob_object[0:15])


# In[ ]:




