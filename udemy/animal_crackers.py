# ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words begin with same letter

def animal_cracker(s):
	words = s.split()
	return words[0][0].lower() == words[1][0].lower()

	
s = input("Enter a string of two words: ")
print(animal_cracker(s))