import nltk


class Virtuant:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('averaged_perceptron_tagger')

    def __tokenize(self, text):
        return nltk.word_tokenize(text)

    def __remove_stopwords(self, tokenized_text):
        stopwords = set(nltk.corpus.stopwords.words('english'))
        filtered_stopwords_text = [word for word in tokenized_text if word not in stopwords]
        return filtered_stopwords_text

    def __pos_tagging(self, tokenized_text):
        return nltk.pos_tag(tokenized_text)

    def  __normalize_words(self, tagged_text):
        stemmer = nltk.stem.snowball.EnglishStemmer()
        normalized_words = list()
        for tagged_word in tagged_text:
            if tagged_word[1] == 'JJS':
                normalized_words.append((stemmer.stem(tagged_word[0].replace('est', '')), 'JJS'))
            elif tagged_word[1] == 'JJR':
                normalized_words.append((stemmer.stem(tagged_word[0].replace('er', '')), 'JJR'))
            else:
                normalized_words.append((stemmer.stem(tagged_word[0]), tagged_word[1]))
        return normalized_words

    def __filter_words(self, tagged_text):
        relevant_words = {'NN', 'NNS', 'NNP', 'JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
        return [tagged_word[0] for tagged_word in tagged_text if tagged_word[1] in relevant_words]

    def ask(self, text):
        tokenized_text = self.__tokenize(text)
        stopwords_removed_text = self.__remove_stopwords(tokenized_text)
        tagged_text = self.__pos_tagging(stopwords_removed_text)
        normalized_text = self.__normalize_words(tagged_text)
        filtered_tagged_text =self.__filter_words(normalized_text)

        return filtered_tagged_text

assistant = Virtuant()
print(assistant.ask('What time does the last bus leave?'))
