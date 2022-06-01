# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a,b):
	return a==20 or b==20 or a+b == 20

	
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print(makes_twenty(a,b))