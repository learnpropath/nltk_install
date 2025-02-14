#a keyword extraction demo
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, num_keywords=5):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w.lower() for w in tokens if not w.lower() in stop_words and w.isalnum]

    # Part-of-speech tagging
    tagged_tokens = pos_tag(filtered_tokens)

    # Extract nouns
    nouns = [word for word, tag in tagged_tokens if tag.startswith('NN')]

    # Calculate TF-IDF (optioanl)
    vectorizer = TfidfVectorizer()
    vectorizer.fit([text])
    tfidf_scores = vectorizer.transform(nouns).toarray()

    # Rank keywords
    ranked_keywords = sorted(zip(nouns, tfidf_scores.flatten()), key=lambda x: x[1], reverse=True)

    # Select top keywords
    top_keywords = [keyword for keyword, score in ranked_keywords[:num_keywords]]


    return top_keywords

# Example usage
text = "This is an example text for keyword extraction using NLTK. It demonstorates the process of tokenization, stop word removal, POS tagging, and noun extraction."
#keywords = extract_keywords(text, 6)
keywords = extract_keywords(text)
print(keywords)


