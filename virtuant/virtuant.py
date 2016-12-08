import nltk

class Virtuant:

    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def __tokenize(self, text):
        return nltk.word_tokenize(text)

    def __remove_stopwords(self, text_tokenized):
        stopwords = set(nltk.corpus.stopwords.words('english'))
        filtered_stopwords_text = [word for word in text_tokenized not in stopwords]
        return filtered_stopwords_text
