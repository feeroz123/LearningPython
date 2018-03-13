# Print out whether entered string is a palindrome or not

ustring = input("Enter any word: ")
chars = list (ustring)

for i in (0, len(chars)-1):
    if chars[len(chars)-1] ==  i :
        flag = 0
    else: flag = 1

if flag == 1:
    print ("Not a Palindrome")
else:
    print ("Palindrome")

