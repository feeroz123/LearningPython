# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(s):
	reversed_string = []
	words_list = s.split()

	for word in words_list:
		reversed_word = word[::-1]
		reversed_string.append(reversed_word)
	return ' '.join(reversed_string)

	
s = input("Enter a sentence: ")
print(master_yoda(s))
