# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

ustring = input("Enter a sentence: ")

splitString = ustring.split(" ")        # Separate the words by " " character
splitString.reverse()                   # Perform reverse operation on the string

print(" ".join(splitString))            # Stitch/Merge the words with " " character in between them
