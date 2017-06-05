from nltk.corpus import cmudict
import nltk



class Book:
    text_title = ''



    def __init__(self, name):
        self.text_title = name

    def total_chars(self):
        with open(self.text_title,'r') as f:
            number_of_chars = 0
            for line in f:
                number_of_chars = number_of_chars + len(line) - line.count('.') - line.count(' ') - line.count(',') - line.count('(') - line.count(')') - line.count('-') - line.count('[') - line.count(']') - line.count(':') - line.count("'")
        return number_of_chars


    def total_word_count(self):
        number_of_words = 0
        with open(self.text_title,'r') as f:
            for line in f:
                words = line.split()
                number_of_words = number_of_words + len(words)

        return number_of_words

    def most_common_words(self):
        greatest_occurence_value = 0
        word_occurences = {}
        most_common_words = {}
        lines = []
        new_lines = []
        words = []
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
            for line in lines:

                line = line.replace(',', '')
                line = line.replace('.', '')
                line = line.replace('!', '')
                line = line.replace('?', '')
                line = line.replace(':', '')
                line = line.replace(';', '')
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace(" '", '')
                line = line.replace("' ", '')
                line = line.replace('-', ' ')
                line = line.replace('\n', '')
                line = line.lower()
                new_lines.append(line)

            # put all the words plus their occurence values in a dictionary
            for line in new_lines:
                temp_words_list = line.split()
                for word in temp_words_list:
                    words.append(word)
            for word in words:
                if word in word_occurences:
                    word_occurences[word] = word_occurences[word] + 1
                else:
                    word_occurences[word] = 1
            # search dictionary for occurence values
            for word in word_occurences:
                if word_occurences[word] > greatest_occurence_value:
                    greatest_occurence_value = word_occurences[word]
            # add the greatest occurence words to their own dictionary
            for word in word_occurences:
                if word_occurences[word] == greatest_occurence_value:
                    most_common_words[word] = greatest_occurence_value
            return most_common_words

    def lexical_density(self):
        with open(self.text_title,'r') as f:
            pass
        f = open(self.text_title).read()
        tokens = nltk.word_tokenize(f)
        word_counter = 0 #counts words
        lex_counter = 0 #counts lexical words
        tokens = nltk.word_tokenize(f) # Converts sentences into words
        for i in nltk.pos_tag(tokens): # for i in the list of tuples
            if i[0] not in [',', '.', ';', '?', '!']: # Checks if i[0] is punctuation, in which case it is skipped
                word_counter += 1
                if i[1] in ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ' ]:
                    lex_counter +=1
        out = lex_counter / word_counter
        return str(out)



    def shortest_words(self):
        shortest_word_length = 99999
        word_lengths = {}
        shortest_words = {}

        lines = []
        new_lines = []
        words = []
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
            for line in lines:

                line = line.replace(',', '')
                line = line.replace('.', '')
                line = line.replace('!', '')
                line = line.replace('?', '')
                line = line.replace(':', '')
                line = line.replace(';', '')
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace(" '", '')
                line = line.replace("' ", '')
                line = line.replace('-', ' ')
                line = line.replace('\n', '')
                line = line.lower()
                new_lines.append(line)

            # put all the words plus their occurence values in a dictionary
            for line in new_lines:
                temp_words_list = line.split()
                for word in temp_words_list:
                    words.append(word)
            for word in words:
                word_lengths[word] = len(word)

            # search dictionary for lengths
            for word in word_lengths:
                if word_lengths[word] < shortest_word_length:
                    shortest_word_length = word_lengths[word]

            for word in word_lengths:
                if word_lengths[word] == shortest_word_length:
                    shortest_words[word] = shortest_word_length
            return shortest_words

    def longest_words(self):
        longest_word_length = 0
        word_lengths = {}
        long_words = {}

        lines = []
        new_lines = []
        words = []
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
            for line in lines:

                line = line.replace(',', '')
                line = line.replace('.', '')
                line = line.replace('!', '')
                line = line.replace('?', '')
                line = line.replace(':', '')
                line = line.replace(';', '')
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace(" '", '')
                line = line.replace("' ", '')
                line = line.replace('-', ' ')
                line = line.replace('\n', '')
                line = line.lower()
                new_lines.append(line)

            # put all the words plus their occurence values in a dictionary
            for line in new_lines:
                temp_words_list = line.split()
                for word in temp_words_list:
                    words.append(word)
            for word in words:
                word_lengths[word] = len(word)

            # search dictionary for lengths
            for word in word_lengths:
                if word_lengths[word] > longest_word_length:
                    longest_word_length = word_lengths[word]

            for word in word_lengths:
                if word_lengths[word] == longest_word_length:
                    long_words[word] = longest_word_length
            return long_words

    def unique_word_count(self):
        word_occurences = {}
        unique_words = []
        lines = []
        new_lines = []
        words = []
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
            for line in lines:

                line = line.replace(',', '')
                line = line.replace('.', '')
                line = line.replace('!', '')
                line = line.replace('?', '')
                line = line.replace(':', '')
                line = line.replace(';', '')
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace(" '", '')
                line = line.replace("' ", '')
                line = line.replace('-', ' ')
                line = line.replace('\n', '')
                line = line.lower()
                new_lines.append(line)

            # put all the words plus their occurence values in a dictionary
            for line in new_lines:
                temp_words_list = line.split()
                for word in temp_words_list:
                    words.append(word)
            for word in words:
                if word in word_occurences:
                    word_occurences[word] = word_occurences[word] + 1
                else:
                    word_occurences[word] = 1
            # add the greatest occurence words to their own dictionary
            for word in word_occurences:
                if word_occurences[word] == 1:
                    unique_words.append(word)
            return unique_words

    def rarest_words(self):
        lowest_occurence_value = 99999
        word_occurences = {}
        least_common_words = {}
        lines = []
        new_lines = []
        words = []
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
            for line in lines:

                line = line.replace(',', '')
                line = line.replace('.', '')
                line = line.replace('!', '')
                line = line.replace('?', '')
                line = line.replace(':', '')
                line = line.replace(';', '')
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace(" '", '')
                line = line.replace("' ", '')
                line = line.replace('-', ' ')
                line = line.replace('\n', '')
                line = line.lower()
                new_lines.append(line)

            # put all the words plus their occurence values in a dictionary
            for line in new_lines:
                temp_words_list = line.split()
                for word in temp_words_list:
                    words.append(word)
            for word in words:
                if word in word_occurences:
                    word_occurences[word] = word_occurences[word] + 1
                else:
                    word_occurences[word] = 1
            # search dictionary for occurence values
            for word in word_occurences:
                if word_occurences[word] < lowest_occurence_value:
                    lowest_occurence_value = word_occurences[word]
            # add the greatest occurence words to their own dictionary
            for word in word_occurences:
                if word_occurences[word] == lowest_occurence_value:
                    least_common_words[word] = lowest_occurence_value
            return least_common_words


    def word_occurence(self):
        word_count = 0
        with open(self.text_title,'r') as f:
            f = f.replace(',', '')
            f = f.replace('.', '')
            f = f.replace('!', '')
            f = f.replace('?', '')
            f = f.replace(':', '')
            f = f.replace(';', '')
            f = f.replace('(', '')
            f = f.replace(')', '')
            f = f.replace(" '", '')
            f = f.replace("' ", '')

            user_input = input("Enter a word to be searched: ")
            words = f.split()
            for word in words:
                if user_input.lower() == word.lower():
                    word_count += 1
        print("Your word " + user_input + " appears " + word_count + " times")
        return word_count

    def num_of_sentences(self):
        number_of_sentences = 0
        with open(self.text_title,'r') as f:
            for line in f:
                number_of_sentences = number_of_sentences + line.count('.')

        # print(number_of_sentences)
        return number_of_sentences

    def average_sentence_length(self):
        lines = []
        total_line_length = 0
        num_of_lines = 0
        average = 0
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
                num_of_lines = num_of_lines + 1
            for line in lines:
                total_line_length = total_line_length + len(line)

        average = total_line_length / num_of_lines
        # print(average)
        return average

    def min_sentence_length(self):
        lines = []
        min_length = 1000
        index = 0
        index_of_min = 0
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
            for line in lines:
                if len(line) < min_length:
                    min_length = len(line)
                    index_of_min = index
                index += 1
        # print(min_length)
        return min_length


    def max_sentence_length(self):
        lines = []
        max_length = 0
        index = 0
        index_of_max = 0
        with open(self.text_title,'r') as f:
            for line in f:
                lines.append(line)
            for line in lines:
                if len(line) > max_length:
                    max_length = len(line)
                    index_of_max = index
                index += 1
        # print(max_length)
        return max_length


    def nsyl(self, word):
        '''This is the primary function for getting syllables
        '''
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
        return counter



    def count_syllables(self):
        # '''This is a function that tries the primary method,
        # and then tries the secondary method
        #  '''
        total_syllables = 0 # the counter starts at 0

        with open(self.text_title,'r') as f: 
            f = open(self.text_title).read()
            tokens = nltk.word_tokenize(f)
            for syl_word in tokens: 
                try:
                    syl_list = self.nsyl(syl_word) # Try the primary method
                    if len(syl_list) == 1: # Sometimes there's an error 
                        total_syllables = total_syllables + syl_list[0]
                    else:
                        total_syllables = total_syllables + self.nsyl_2(syl_word)
                except:
                    total_syllables = total_syllables + self.nsyl_2(syl_word)
            return total_syllables


    def ari_score(self):
        number_of_sentences = 0
        number_of_words = 0
        number_of_chars = 0
        automated_readability_index = 0
        ari_scale = {
             1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
             2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
             3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
             4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
             5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
             6: {'ages': '10-11', 'grade_level':    '5th Grade'},
             7: {'ages': '11-12', 'grade_level':    '6th Grade'},
             8: {'ages': '12-13', 'grade_level':    '7th Grade'},
             9: {'ages': '13-14', 'grade_level':    '8th Grade'},
            10: {'ages': '14-15', 'grade_level':    '9th Grade'},
            11: {'ages': '15-16', 'grade_level':   '10th Grade'},
            12: {'ages': '16-17', 'grade_level':   '11th Grade'},
            13: {'ages': '17-18', 'grade_level':   '12th Grade'},
            14: {'ages': '18-22', 'grade_level':      'College'}
        }

        with open(self.text_title,'r') as f:
            for line in f:
                words = line.split()
                number_of_sentences = number_of_sentences + line.count('.') # 3 variables about sentences
                number_of_words = number_of_words + len(words)
                number_of_chars = number_of_chars + len(line) - line.count('.') - line.count(' ') - line.count(',') - line.count('(') - line.count(')') - line.count('-') - line.count('[') - line.count(']') - line.count(':')

            automated_readability_index = (4.71) * (number_of_chars/number_of_words) + (0.5) * (number_of_words/number_of_sentences) - 21.43

            # print(str(number_of_words) + " words")
            # print(str(number_of_chars) +" characters")
            # print(str(number_of_sentences) + " sentences")
            # print(str(automated_readability_index) + " is its ARI")
            automated_readability_index = int(automated_readability_index)
            if automated_readability_index > 14:
                automated_readability_index = 14
            # print("Ages: " + ari_scale[automated_readability_index]['ages'] + " Grade:" + ari_scale[automated_readability_index]['grade_level'])
            # print("")
            return automated_readability_index


    def output_report(self):
        with open('book_output_report.txt', 'w') as new_file:
            new_file.write('')
        with open('book_output_report.txt', 'w') as new_file:
            new_file.write("The total character count is: " + str(self.total_chars()) + "\n")
            new_file.write("The total word count is: " + str(self.total_word_count()) + "\n")
            new_file.write("The most common word(s) are: " + str(self.most_common_words()) + "\n")
            new_file.write("The lexical density is: " + str(self.lexical_density()) + "\n")
            new_file.write("The shortest word(s) are: " + str(self.shortest_words()) + "\n")
            new_file.write("The longest word(s) are: " + str(self.longest_words()) + "\n")
            new_file.write("The unique (1 occurence) word(s) are: " + str(self.unique_word_count()) + "\n")
            new_file.write("The least common word(s) are: " + str(self.rarest_words()) + "\n")
            new_file.write("The total number of sentences is: " + str(self.num_of_sentences()) + "\n")
            new_file.write("The average sentence length is: " + str(self.average_sentence_length()) + "\n")
            new_file.write("The minimum sentence length is: " + str(self.min_sentence_length()) + "\n")
            new_file.write("The maximum sentence length is: " + str(self.max_sentence_length()) + "\n")
            new_file.write("The total number of syllables is: " + str(self.count_syllables()) + "\n")
            new_file.write("The ARI is: " + str(self.ari_score()) + "\n")



new_book = Book('gettysburg_address.txt')
new_book.output_report()
