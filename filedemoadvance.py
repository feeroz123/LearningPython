with open("file2.txt", "w") as file:
    file.write("This is first line")
    file.write("\nThis is second line")

with open("file2.txt", "r") as file:
    print(str(file.read()))

with open("file2.txt", "w") as file:
    file.write("\nThis is new line")

with open("file2.txt", "a") as file:
    file.write("\nThis is another new line")

with open("file2.txt", "r") as file:
    print(str(file.read()))


