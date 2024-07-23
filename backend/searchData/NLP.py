import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
import numpy as np

stemmer = PorterStemmer()

def tokenize(word):
    return nltk.word_tokenize(word)

def stemming(word):
    return stemmer.stem(str.lower())

def bag_of_words(tok_str, words):
    idx = 0
    bag = np.zeros(len(words))
    tok_str = [stemming(word) for word in tok_str]
    for word in words:
        if word in tok_str:
            bag[idx] = 1
        idx += 1 
    return bag