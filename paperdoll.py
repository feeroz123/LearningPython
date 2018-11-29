# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def paper_doll(s):
	letters = list(s)
	print(''.join([i*3 for i in letters]))
	
s = input("Enter a string: ")
paper_doll(s)