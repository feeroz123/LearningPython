def check_palindrome_num(num):
    quo = int(num/10)     # Conversion to INTEGER is Important here to avoid quo generation as FLOAT value
    rem = num % 10
    revert = 0
    while rem > 0:
        revert = revert * 10 + rem
        rem = quo % 10
        quo = int(quo/10)  # Conversion to INTEGER is Important here to avoid quo generation as FLOAT value
    print("Reverted Number is : ", str(revert))
    if revert == num:
        print(num, "is a Palindrome")
    else:
        print("Not a Palindrome")


num = int(input("Enter a number: "))
check_palindrome_num(num)
