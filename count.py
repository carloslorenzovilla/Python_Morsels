# I want you to write a function that accepts a string 
# and returns a mapping (a dictionary or dictionary-like structure) 
# that has words as the keys and the number of times each word was 
# seen as the values.

import re
from collections import Counter

def count_words(string_):
    """ Returns the count of each word in a string

        string_: string

        returns: Counter object
    """
    regex = r"[\w'-]+"
    list_ = re.findall(regex, string_.lower())
    counter = Counter(list_)
    return counter
