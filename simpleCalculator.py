firstNum = int(input("Enter first Number: "))
secondNum = int(input("Enter second Number: "))
operator = input("Enter the operator: ")

if operator == '+':
    print("Sum = ", firstNum + secondNum)
elif operator == '-':
    print("Difference is: ", firstNum - secondNum)
elif operator == '*':
    print("Product is: ", firstNum * secondNum)
elif operator == '/':
    print("Division is: ", firstNum / secondNum)
elif operator == '^' or operator == '**':
    print("Powered value is: ", firstNum ** secondNum)
else:
    print("Invalid input")
