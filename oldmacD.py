# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_mac_donald(name):
	list_name = list(name)
	list_name[0] = list_name[0].upper()
	list_name[3] = list_name[3].upper()
	return ''.join(list_name)

name = input("Enter a name: ")
print(old_mac_donald(name))