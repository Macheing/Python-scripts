'''
The highlight_word function changes the given word in
a sentence to its upper-case version
'''

def highlight_word(sentence, word):
	senten = sentence.split()
	#print(senten)
	statement = ''
	for sen in senten:
		if sen == word:
			#print(sen)
			statement = str(sentence).replace(sen,word.upper())
		elif sen.endswith('!'):
			sen = str(sen).replace('!','')
			statement = str(sentence).replace(sen,word.upper())
		
	return statement

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
