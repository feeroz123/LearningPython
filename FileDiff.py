with open("file1.txt", "r") as f1:
    f1_data = f1.readlines()
print(f1_data)
print("--------------------------------------------")

with open("file2.txt", "r") as f2:
    f2_data = f2.readlines()
print(f2_data)
print("--------------------------------------------")

for line1 in f1_data:
    if line1 not in f2_data:
        print(line1)


