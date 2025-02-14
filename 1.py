# A simple demo for tokenization
import nltk
#nltk.download()

text = """Welcome you to programming knowlege. Let's start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""

from nltk.tokenize import word_tokenize
word_tokenized = word_tokenize(text)
print(word_tokenized)

from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))

from nltk.probability import FreqDist
print(FreqDist(word_tokenized))