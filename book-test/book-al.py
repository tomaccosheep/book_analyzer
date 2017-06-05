
# from nltk.corpus import cmudict
# import nltk

import nltk


class Book:
    text_title = ''



    def __init__(self, name):
        self.text_title = name


    def lexical_density(self):
        with open(self.text_title,'r') as f:
            pass
        f = open(self.text_title).read()
        word_counter = 0 #counts words
        lex_counter = 0 #counts lexical words
        tokens = nltk.word_tokenize(f) # Converts sentences into words
        for i in nltk.pos_tag(tokens): # for i in the list of tuples
            if i[0] not in [',', '.', ';', '?', '!']: # Checks if i[0] is punctuation, in which case it is skipped
                word_counter += 1
                if i[1] in ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ' ]:
                    lex_counter +=1
        return [word_counter, lex_counter]





    def nsyl(self, word):
        '''This is the primary function for getting syllables
        '''
        print('nsyl')
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

    def nsyl_2(self, word):
        '''This is the backup function for getting syllables
        '''
        chars = [] # an empty set of characters
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'y'] # list of vowels to check against
        counter = 0 
        for i in word:
            chars.append(i) #turn the word into a list of characters
        if chars[-1] != 'e' and chars[-1] in vowel_list: #check for words that end in 'e' or another vowel
            # my algorithm would miss a final vowel, so this part adds
            # if there is a final vowel
            counter += 1
        if chars[-2:] == ['e', 'd'] and len(chars) > 4 and chars[-3] not in ['d', 't']: #different rules for words that end in 'ed'
            counter -= 1
        for i in range(1, len(chars)):
            if chars[i] not in vowel_list:
                if chars[i - 1] in vowel_list:
                    counter += 1 # adds one if a character isn't a vowel, but the previous one is a vowel
        print('nsyl2')
        return counter



    def count_syllables(self):
        # '''This is a function that tries the primary method,
        # and then tries the secondary method
        #  '''
        total_syllables = 0 # the counter starts at 0
        with open(self.text_title,'r') as f:
            f = open(self.text_title).read()
            tolkens = nltk.word_tokenize(f) # Converts sentences into words
            for syl_word in tolkens:
                print(syl_word)
                try:
                    syl_list = self.nsyl(syl_word) # Try the primary method
                    if len(syl_list) == 1: # Sometimes there's an error 
                        total_syllables = total_syllables + syl_list[0]
                    else:
                        total_syllables = total_syllables + self.nsyl_2(syl_word)
                except:
                    total_syllables = total_syllables + self.nsyl_2(syl_word)
            return total_syllables




new_book = Book('gettysburg_address.txt')
