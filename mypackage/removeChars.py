# To remove characters from a string

mystring = 'www.edureka.in'

# Remove all w’s before and after .edureka.
print("Remove all w's => ", mystring.strip('www'))

# Remove all lowercase letter before and after .edureka.
print('Remove all lowercase letter before and after .edureka. => ', '.' + mystring.split('.', 2)[1] + '.')

# Remove all printable characters
print("Remove all printable characters => ", ''.join([x for x in mystring if not x.isprintable()]))

