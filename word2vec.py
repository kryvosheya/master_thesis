#!/bin/bash
import nltk
from gensim.models import Word2Vec

file = open('general_ru', "r")
input_text = file.read()

processed_article = input_text.lower()


# Replaces escape character with space
processed_article = processed_article.replace("\n", " ")

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)
#print(all_sentences)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
model = Word2Vec(all_words, min_count=3, sg = 1, size = 300 )



# summarize the loaded model
print(model)
# summarize vocabulary
# save model
model.save('word2vec_russian_general.bin')
