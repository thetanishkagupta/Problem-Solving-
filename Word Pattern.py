# there is a bijection between a letter in pattern and a non-empty word in s.

class Solution(object):
    def wordPattern(self, pattern, s):
        map_char = {}  # for mapping character
        map_word = {}  # for mapping word to character
        word_list = s.split()  # splitting list of strings with spaces
        if(len(pattern) != len(word_list)):
            return False
        
        # zip function is used for extracting first character from pattern and word_list and giving it in the loop 
        for character , word in zip(pattern , word_list):
            if character not in map_char:
                if word in map_word:
                    return False
                else:
                    map_char[character] = word
                    map_word[word] = character
            else:
                if(map_char[character] != word):
                    return False
        return True       
