# Writing into a file

with open('file1.txt','w') as open_file:
    open_file.write('Hello Boss !')

print("File is written")

with open('file1.txt','r') as open_file:
    print(open_file.read())
