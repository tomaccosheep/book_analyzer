from nltk.corpus import cmudict
d = cmudict.dict()



def nsyl(word):
	'''This is the primary function for getting syllables
	'''
	print('nsyl')
	return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

def nsyl_2(word):
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
	


def syl_num(syl_word):
	'''This is a function that tries the primary method,
	and then tries the secondary method
	'''
	try:
		syl_list = nsyl(syl_word)
		if len(syl_list) == 1:
			return syl_list[0]
		else:
			return nsyl_2(syl_word)
	except:
		return nsyl_2(syl_word)



while True:
	'''This is a while loop to test it
	'''
	a = input(':')
	print(syl_num(a))


