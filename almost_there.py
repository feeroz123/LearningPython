# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
	return 0<=100-n<=10 or 0<=200-n<=10
	
n = int(input("Enter an integer: "))
print(almost_there(n))