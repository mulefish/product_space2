import nltk
from nltk.corpus import words

def is_english_word(word):
    # Check if the word is in the English words corpus
    return word.lower() in words.words()

def split_description(description):
    # Split the description on non-word characters
    words = nltk.word_tokenize(description)
    english_words = []
    non_english_words = []

    for word in words:
        # Check if the remaining text is an English word or not
        if is_english_word(word):
            english_words.append(word)
        else:
            non_english_words.append(word)

    return english_words, non_english_words

# Example usage
descriptions = ["This is a product description.", "I hope it works well!", "Illegitimate word flabbergasted xyz."]

for description in descriptions:
    english_words, non_english_words = split_description(description)
    print(f"English words: {english_words}")
    print(f"Non-English words: {non_english_words}")
    print()
