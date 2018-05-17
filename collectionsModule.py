# Counter
print('COUNTER')
from collections import Counter
a = [1,1,1,3,4,5,7,7,1,5,4,7,9,0,4,2,1,2,4,3,1,5,6,8,0]
print(Counter(a))
s = ['t', 'r', 'i', 't', 't', 'r', 'y']
print(Counter(s))

# defaultdict
print('\n DEFAULTDICT')
from collections import defaultdict
a = defaultdict(int)        # The default data type is set as Integer.
#a = {'k1':1, 'k2':2, 'k3':3}
print(a)        # print the contents of dictionary a
print(a['k2'])  # print the value of key k2 (non existent) from dictionary a. The default Integer value for the non existent keys get assigned and stored in dictionary
print(a['k4'])  # print the value of key k4 (non existent) from dictionary a. The default Integer value for the non existent keys get assigned and stored in dictionary
print(a)        # print the updated contents of dictionary a

# OrderedDict
print('\n ORDEREDDICT')
from collections import OrderedDict
d = OrderedDict()       # Ordered Dictionary
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
d['k4'] = 4
d['k5'] = 5

for k,v in d.items():
    print(k,v)

print('\n')
d1 = OrderedDict()      # Ordered Dictionary
d1['k1'] = 1
d1['k3'] = 3
d1['k4'] = 4
d1['k5'] = 5
d1['k2'] = 2

print('\n')
d2 = {}                 # Non Ordered Dictionary
d2['k1'] = 1
d2['k2'] = 2
d2['k3'] = 3
d2['k4'] = 4
d2['k5'] = 5

for k,v in d1.items():
    print(k,v)

print(d == d1)      # Returns FALSE (for Order dcitionaries) as the order of entries made in d is not same as in d1, even though the entries are same
print(d == d2)      # Returns TRUE (comparison of Orderd and Non ordered dictionaries) as the entries in d is same as in d2, even though the order of entries is not same

# namedtuple
print('\n NAMEDTUPLE')
from collections import namedtuple
t = ('John','Dog',2)        # Normal tuple
print(t)
print(t[1])         # To fetch the value present at index 1
print('\n')
sample = namedtuple('sample', 'name pet count')    # SYNTAX ==> ClassName = namedtuple('ClassName', 'field1name field2name field3name ...')
t2 = sample(name='John', pet='Dog', count=2)       # SYNTAX ==> ObjectName = ClassName(field1name = 'value1', field2name = 'value2', field3name = 'value3', ...')
print(t2.name)      # Called the value of name field stored in object t2 of class sample
print(t2.pet)       # Called the value of pet field stored in object t2 of class sample
print(t2[2])        # Called the value of stored at index 2 of object t2 of class sample