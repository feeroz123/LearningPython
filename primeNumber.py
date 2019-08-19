# Function to find if entered number is Prime or Composite

u = 0
flag = 0

while u < 2:
    u = int(input("Enter a number: "))

if u > 2:
   for i in range(2, u):
        if u % i == 0:
            flag = 1
            break

if flag == 1:
    print("Composite")
else:
    print("Prime")