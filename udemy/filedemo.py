"""
Reading and writing files
"""

my_file = open("file1.txt", "w")
my_file.write("This is first line.")
my_file.close()

my_file = open("file1.txt", "r")
print(str(my_file.read()))
my_file.close()

my_file = open("file1.txt", "a")
my_file.write("\nThis is second line.")
my_file.close()

my_file = open("file1.txt", "r")
print(str(my_file.read()))
my_file.close()