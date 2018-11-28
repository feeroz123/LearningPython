# Function to take two numbers. Print lesser of the numbers if both are even, else print greater of the numbers if both are odd.

def even_or_odd(inputs):
    if inputs[0] % 2 == 0 and inputs[1] % 2 == 0:
        return "Lesser of the given numbers: ", min(inputs[0], inputs[1])
    elif inputs[0] % 2 != 0 and inputs[1] % 2 != 0:
        return "Greater of the given numbers: ", max(inputs[0], inputs[1])
    else:
        return "other"


input_values = []
input_values.append(int(input("Enter first number: ")))
input_values.append(int(input("Enter second number: ")))

if input_values[0] == input_values[1]:
    print("Equal integers were entered.")
else:
    print(even_or_odd(input_values))
