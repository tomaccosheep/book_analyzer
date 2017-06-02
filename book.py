class Book:
    text_title = ''



    def __init__(self, name):
        self.text_title = name

    def total_chars(self):
        with open(self.text_title,'r') as f:
            number_of_chars = 0
            for line in f:
                number_of_chars = number_of_chars + len(line) - line.count('.') - line.count(' ') - line.count(',') - line.count('(') - line.count(')') - line.count('-') - line.count('[') - line.count(']') - line.count(':') - line.count("'")

    def total_word_count(self):
        with open(self.text_title,'r') as f:
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
                number_of_words = number_of_words + len(words)
                print(number_of_words)
                return number_of_words

    def most_common_words(self):
        greatest_occurence_value = 0
        word_occurences = {}
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
        with open(self.text_title,'r') as f:

    def shortest_words(self):
        shortest_word_length = 0
        word_lengths = {}
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

        print(number_of_sentences)
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
        print(average)
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
        print(min_length)
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
        print(max_length)
        return max_length


    def count_syllables(self):
        with open(self.text_title,'r') as f:

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

            print(str(number_of_words) + " words")
            print(str(number_of_chars) +" characters")
            print(str(number_of_sentences) + " sentences")
            print(str(automated_readability_index) + " is its ARI")
            automated_readability_index = int(automated_readability_index)
            if automated_readability_index > 14:
                automated_readability_index = 14
            print("Ages: " + ari_scale[automated_readability_index]['ages'] + " Grade:" + ari_scale[automated_readability_index]['grade_level'])
            print("")


        def output_report(self):
            with open(self.text_title,'r') as f:
