#lower()
string_ = 'Its not PROPER'
print(string_.lower())

#upper()
string_ = 'Its not PROPER'
print(string_.upper())

#count()
string_ = 'This is the is for a loc a for'
print(string_.count('for'))
print(string_.count('is'))
print(string_.count('i'))

#find()
"return the position of a substring pr character where it is found"
"returns -1 if the string not found"
string_ = 'This is the is for a loc a for'

print(string_.find('for'))
print(string_.find('r'))

#rfind
"checks for a character or string from the end of the string"
"it will give the postive index values only"
string_ = 'This is the is for a loc a for'
print(string_.rfind('is'))
print(string_.rfind('i'))



#index
"returns the index of the specified sub string or character"
"returns value error if the sub string npt fouind"
string_ = 'This si Mohana Kasi'
print(string_.index('Mohana'))
print(string_.index('i'))

#rindex
"return"