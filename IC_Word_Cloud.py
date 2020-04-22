"""You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the
body of text.
* While counting capitalization should be disregarded from being a different word. i.e. After and after should = 2

Steps
1. Splitting the words from the input string
2. Populating the dictionary with each word
3. Handling words that are both uppercase and lowercase in the input string

We could use split() but if we split on spaces then we'd have to iterate over all the words before and after splitting
to clean up the punctuation (dashes and hyphens etc.) which aren't surrounded by spaces but nonetheless are separate
words. SO I'm going to make my own split method.
"""

# Split the words from the input string
def split_words(input_string):
    words = []
    current_word_index = 0
    current_word_length = 0

    for i, char in enumerate(input_string):
        if char.isalpha():
            if current_word_length == 0:
                current_word_index = i
            current_word_length += 1
        else:
            word = input_string[current_word_index: current_word_index + current_word_length]
            words.append(word)
            current_word_length = 0

    return words

# Populate the dictionary with each word

def add_to_dict(word):
    words_to_counts = {}
    if word in words_to_counts:
        words_to_counts[word] += 1
    else:
        words_to_counts[word] = 1
    return words_to_counts

#
