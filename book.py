<<<<<<< HEAD
# from nltk.corpus import cmudict
# import nltk
=======
import nltk
>>>>>>> d4fa31ee7a1e8e3dee298c3c441487e8dbce3f8c

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
<<<<<<< HEAD
            with open(self.text_title,'r') as f:
                for line in f:
                    words = line.split()
                    number_of_words = number_of_words + len(words)
=======
			 for line in file:
		        print(line.replace(',', ''), end='')
		        print(line.replace('.', ''), end='')
		        print(line.replace('!', ''), end='')
		        print(line.replace('?', ''), end='')
		        print(line.replace(':', ''), end='')
		        print(line.replace(';', ''), end='')
		        print(line.replace('(', ''), end='')
		        print(line.replace(')', ''), end='')
		        print(line.replace(' \'', ''), end='')
		        print(line.replace('\' ', ''), end='')

                # put all the words plus their occurence values in a dictionary
                words = f.split()
                number_of_words = 0
                number_of_words = number_of_words + len(words)
>>>>>>> d4fa31ee7a1e8e3dee298c3c441487e8dbce3f8c
                # print(number_of_words)
                return number_of_words

    def most_common_words(self):
        greatest_occurence_value = 0
        word_occurences = {}
        most_common_words = {}
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

            # put all the words plus their occurence values in a dictionary
            words = f.split()
            for word in words:
                if word in word_occurences:
                    word_occurences[word] = word_occurences[word] + 1
                else:
                    word_occurences[word] = 1

            # search dictionary for occurence values
            for word in word_occurences:
                if word_occurences[word] > greatest_occurence_value:
                    greatest_occurence_value = word_occurences[word]

            print("Your rarest words are: ")
            for word in word_occurences:
                if word_occurences[word] == greatest_occurence_value:
                    print(word)
            print("With " + greatest_occurence_value + "occurence(s) each")

    def lexical_density(self):
<<<<<<< HEAD
        with open(self.text_title,'r') as f:
            pass
=======
		f = open("myfile.txt").read()
		tokens = nltk.word_tokenize(f)
		word_counter = 0 #counts words
		lex_counter = 0 #counts lexical words
		tokens = nltk.word_tokenize(words)
		for i in nltk.pos_tag(tokens): # for i in the list of tuples
			#if i not in [',', '.', ';', '							 # (word, word type) (run, VB)
			word_counter += 1
			if i[1] in ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ' ]:
				lex_counter +=1
		return [word_counter, lex_counter]






>>>>>>> d4fa31ee7a1e8e3dee298c3c441487e8dbce3f8c
    def shortest_words(self):
        shortest_word_length = 0
        word_lengths = {}
        shortest_words = {}
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

            # put all the words plus their length values in a dictionary
            words = f.split()
            for word in words:
                word_lengths[word] = len(word_lengths[word])

            # search dictionary for lengths
            for word in word_lengths:
                if word_lengths[word] < shortest_word_length:
                    shortest_word_length = word_lengths[word]

            print("Your shortest word(s) are: ")
            for word in word_lengths:
                if word_lengths[word] == shortest_word_length:
                    print(word)
            print("All being " + shortest_word_length + " long")

    def longest_words(self):
        longest_word_length = 0
        word_lengths = {}
        longest_words = {}
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

            # put all the words plus their length values in a dictionary
            words = f.split()
            for word in words:
                word_lengths[word] = len(word_lengths[word])

            # search dictionary for lengths
            for word in word_lengths:
                if word_lengths[word] > longest_word_length:
                    longest_word_length = word_lengths[word]

            print("Your longest word(s) are: ")
            for word in word_lengths:
                if word_lengths[word] == longest_word_length:
                    print(word)
            print("All being " + longest_word_length + " long")

    def unique_word_count(self):
        word_occurences = {}
        unique_words = {}
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

            # put all the words plus their occurence values in a dictionary
            words = f.split()
            for word in words:
                if word in word_occurences:
                    word_occurences[word] = word_occurences[word] + 1
                else:
                    word_occurences[word] = 1

            print("Your unique(1 occurence) words are: ")
            for word in word_occurences:
                if word_occurences[word] == 1:
                    print(word)

    def rarest_words(self):
        lowest_occurence_value = 99999
        word_occurences = {}
        rarest_words = {}
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

            # put all the words plus their occurence values in a dictionary
            words = f.split()
            for word in words:
                if word in word_occurences:
                    word_occurences[word] = word_occurences[word] + 1
                else:
                    word_occurences[word] = 1

            # search dictionary for occurence values
            for word in word_occurences:
                if word_occurences[word] < lowest_occurence_value:
                    lowest_occurence_value = word_occurences[word]

            print("Your rarest words are: ")
            for word in word_occurences:
                if word_occurences[word] == lowest_occurence_value:
                    print(word)
            print("With " + lowest_occurence_value + "occurence(s) each")

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
    	print('nsyl')
    	return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

    def nsyl_2(self, word):
    	'''This is the backup function for getting syllables
    	'''
    	chars = []
    	vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    	counter = 0
    	for i in word:
    		chars.append(i)
    	if chars[-1] != 'e' and chars[-1] in vowel_list:
    		counter =+ 1
    	if chars[-2:] == ['e', 'd'] and len(chars) > 4 and chars[-3] not in ['d', 't']:
    		counter -= 1
    		print('aaa')
    	for i in range(1, len(chars)):
    		if chars[i] not in vowel_list:
    			if chars[i - 1] in vowel_list:
    				counter += 1
    	print('nsyl2')
    	return counter



    def count_syllables(self):
    	# '''This is a function that tries the primary method,
    	# and then tries the secondary method
    	#  '''
        total_syllables = 0
        with open(self.text_title,'r') as f:
            for line in f:
                for syl_word in line:
                    try:
                        syl_list = nsyl(syl_word)
                        if len(syl_list) == 1:
                            total_syllables = total_syllables + syl_list[0]
                        else:
                            total_syllables = total_syllables +nsyl_2(syl_word)
                    except:
                        total_syllables = total_syllables + nsyl_2(syl_word)
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
            new_file.write(self.most_common_words() + "\n")
            # new_file.write("The lexical density is: " + str(self.lexical_density()) + "\n")
            # new_file.write(self.shortest_words() + "\n")
            # new_file.write(self.longest_words() + "\n")
            # new_file.write(self.unique_word_count() + "\n")
            # new_file.write(self.rarest_words() + "\n")
            new_file.write("The total number of sentences is: " + str(self.num_of_sentences()) + "\n")
            new_file.write("The average sentence length is: " + str(self.average_sentence_length()) + "\n")
            new_file.write("The minimum sentence length is: " + str(self.min_sentence_length()) + "\n")
            new_file.write("The maximum sentence length is: " + str(self.max_sentence_length()) + "\n")
            # new_file.write("The total number of syllables is: " + str(self.count_syllables()) + "\n")
            new_file.write("The ARI is: " + str(self.ari_score()) + "\n")



new_book = Book('gettysburg_address.txt')
new_book.output_report()
