import unicodedata

def remove_accent(string):
    return unicodedata.normalize('NFKD', string)

def is_anagram(word1, word2):

    def get_letters(string):
        string = remove_accent(string.lower())
        return sorted(
            x for 
            x in string 
            if x.isalpha())
    
    return get_letters(word1) == get_letters(word2)
