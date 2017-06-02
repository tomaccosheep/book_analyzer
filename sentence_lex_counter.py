import nltk
test_sen = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(test_sen)
word_counter = 0 #counts words
lex_counter = 0 #counts lexical words
for i in nltk.pos_tag(tokens): # for i in the list of tuples
								 # (word, word type) (run, VB)
	word_counter += 1
	if i[1] in ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ' ]:
		print('Lex ' + str(i[0]))
		lex_counter +=1

print('Words: ', str(word_counter), '\nLex ', str(lex_counter))
