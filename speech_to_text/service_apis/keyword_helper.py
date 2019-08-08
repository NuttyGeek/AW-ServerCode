# importing stuff we need
import nltk
# before importing we need to download it
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def filter_sentence(sentence=None):
    """
    this fxn takes a sentence and remove stop words from it and return it as a list
    Parameters: sentence - string sentence to be filtered
    Return: a list of string after removing the stopwords
    """
    # empty string
    result = []
    # get all the words in sentence
    words = word_tokenize(sentence)
    # get all the stop words
    stop_words = set(stopwords.words("english"))
    for w in words:
        if w not in stop_words:
            result.append(w)
            print(result)
    return result

