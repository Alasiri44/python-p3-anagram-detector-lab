import re

# creating an anagram class

class Anagram:
    def __init__(self, word):
        self.word = word
        
    # @property
    # def word(self):
    #     return self._word

    def match(self,input_list):       
        matching_words = []
        word_given = []
        list_given = []
        for letter in self.word:
            word_given.append(letter)
            
        for n in input_list:
            for letter in n:
                list_given.append(letter)
                       
            if sorted(list_given) == sorted(word_given):               
               matching_words.append(n)
            else:
                pass
            list_given.clear()
                
        print(matching_words)
        return matching_words     

Anagram("enlist").match(["listen", "silent", "hippopotamus"])