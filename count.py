# I want you to write a function that accepts a string 
# and returns a mapping (a dictionary or dictionary-like structure) 
# that has words as the keys and the number of times each word was 
# seen as the values.

import re

def count_words(string_):
    regex = r'(\b\w+[\']\w+\b|\b\w+\b)'
    string_ = re.findall(regex, string_)
    dict_ = {}
    for word in string_:
        word = word.lower()
        dict_[word] = 1 + dict_.get(word, 0)
    return dict_