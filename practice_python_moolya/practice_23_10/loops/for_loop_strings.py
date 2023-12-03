""'print 1 to 10using for loop""'
for num in range(1,11):
    print(num, end=' ')
print()
"""print 10 to 1 using for loop"""
for num in range(10, 0, -1):
    print(num, end=' ')
print()
"""print -1 to -10 using for"""
for num in range(-1, -11, -1):
    print(num, end=' ')
print()
"""print even numbers using for loop"""
for num in range(0, 20, 2):
    print(num, end=' ')
print()
"""trravels throuh string using for loop"""
string_ = 'This is python'
for index in range(len(string_)):
    print(string_[index], end='')
print()
"""trravels throuh string using for loop (appending string istead of range())"""
string_ = 'This is python'
for char in string_:
    print(char, end = '')
print()
""" traversing through dictionaries """
dict_ = {'name': 'kasi', 'loc':'bangalore', 'id': 1008}
for key in dict_:
    print(key, '--->', dict_[key], end=' ')
print()

for key, value in dict_.items():
    print(print(key, '--->', value, end=' '))
print()
"""unpacking"""
a=[1,2,3,4]
n1, *mid, n2 = a
print(n1, n2, mid)

""" traversing a string in reversed order """
for index in range(-1, -(len(string_)+1), -1):
    print(string_[index], end=' ')


for item in range(len(string_)-1, -1, -1):
    print(string_[item], end=" ")

print()

