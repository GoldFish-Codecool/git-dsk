import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

nltk.download('punkt')

def text_statistics(text):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Calculate word count and sentence count
    word_count = len(words)
    sentence_count = len(sentences)

    # Calculate average word length
    total_word_length = sum(len(word) for word in words)
    average_word_length = total_word_length / word_count if word_count > 0 else 0

    # Count the frequency of each word
    word_freq = Counter(words)

    # Find common words (top N most frequent words)
    common_words_count = 10  # Change this number as needed
    common_words = word_freq.most_common(common_words_count)

    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'average_word_length': average_word_length,
        'common_words': common_words
    }

if __name__ == "__main__":
    text = """Enter your text here. This is just an example text that you can replace with your own text. 
    You can use multiple sentences and words in this text to see the statistics."""
    
    stats = text_statistics(text)

    print(f"Word Count: {stats['word_count']}")
    print(f"Sentence Count: {stats['sentence_count']}")
    print(f"Average Word Length: {stats['average_word_length']:.2f}")
    print("Common Words:")
    for word, frequency in stats['common_words']:
        print(f"{word}: {frequency}")
