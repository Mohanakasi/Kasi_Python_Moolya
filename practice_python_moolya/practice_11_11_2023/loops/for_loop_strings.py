""'print 1 to 10using for loop""'
for num in range(1,11):
    print(num)
"""print 10 to 1 using for loop"""
for num in range(10, 0, -1):
    print(num, end=' ')
"""print -1 to -10 using for"""
for num in range(-1, -11, -1):
    print(num, end=' ')

"""print even numbers using for loop"""
for num in range(0, 20, 2):
    print(num, end=' ')

"""trravels throuh string using for loop"""
string_ = 'kasi is a king'
for char in string_:
    print(char, end=' ')
for index in range(len(string_)):
    print(string_[index], end=' ')

""" count the number of characters in a string """
string_ = "hello world"
count = 0
for char in string_:
    count += 1
print(count)

"""print even characters in a string"""
string_ = "hello world"
for index in range(0, len(string_), 2):
    print(string_[index], end=' ')

"""to print the digits in a string using inbuilt method"""
s= 'kasi 123'
for char in s:
    if char.isdigit():
        print(char)

"""to print the digits in a string wuthout using inbuilt method"""
for char in s:
    if '0'<=char<='9':
        print(char, end=' ')
"""to count no of special characters in a string"""
string_ = 'kasi123@$$$.%+'
count = 0
for char in string_:
    if 'a'<=char<='z' or 'A'<=char<='Z' or '0'<=char<='9':
        pass
    else:
        count += 1
print(count)

"""to count capital and small letters in a string"""
string_ = 'KASI is from GUNTUR'
count_cap = 0
count_small = 0
for char in string_:
    if 65<=ord(char)<=90:
        count_cap += 1
    elif 97<=ord(char)<=122:
        count_small += 1
print(count_small, count_cap)

