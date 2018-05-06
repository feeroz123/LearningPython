from typing import List

my_pattern = [1,2,3]
success_pattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]


noted_pattern = ['', 'o', 'o', 'o', 'x', 'x', 'x', 'w', 'w', 'w']
pattern_x = []
pattern_o = []
for counter, value in enumerate(noted_pattern):
    if value == 'x':
        pattern_x.append(counter)
    elif value == 'o':
        pattern_o.append(counter)

for i in range(0,len(pattern_x)):
    print('Pattern X = ', pattern_x[i])

for i in range(0,len(pattern_o)):
    print('Pattern O = ', pattern_o[i])


if pattern_x in success_pattern:
    print("SUCCESS of X")

if pattern_o in success_pattern:
    print("SUCCESS of O")
else:
    print('NO SUCCESS')