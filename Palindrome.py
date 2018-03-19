# Print out whether entered string is a palindrome or not

ustring = input("Enter any word: ")

reverseString = ustring[::-1]       # Advanced Slice function to return values with step value as -1

print("Reverse is :", reverseString)

if reverseString == ustring:
    print("Palindrome")
else:
    print("Not Palindrome")



