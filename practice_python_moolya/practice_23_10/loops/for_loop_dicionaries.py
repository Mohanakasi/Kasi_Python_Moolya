"""traversing through dictionary directly"""
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key in d:
    print(key, d[key])
"""printing keys using keys inbuilt method  """
for key in d.keys():
    print(key)
"""printing keys using items inbuilt method"""
for key, value in d.items():
    print(key)

"""print values in a dictionary"""
for value in d.values():
    print(value)

"""print values in a dictionary using get method"""
for key in d.keys():
    print(d.get(key))

"""print values in a dictionary  using enumerate class"""
for index, (key, value) in enumerate(d.items()):
    print(key, value)

"""printing characters and its count of a string into dictionary 
uisng inbuilt method count"""
string_ = 'This is pythons world'
d= {}
for char in string_:
    d[char] = string_.count(char)

print(d)
"""printing characters and its count of a string into dictionary 
without using inbuilt method (if - else)"""
string_ = 'This is pythons world'
d = {}
for char in string_:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

print(d)

"""printing characters and its count of a string 
into dictionary using inbuilt class defaultdict"""
from collections import defaultdict
d = defaultdict(int)
for char in string_:
    d[char] += 1
print(d)
"""counting no words in a string and printing with word and count into  a dictionary 
using without inbuilt (if-else)"""
d = {}
for word in string_.split():
    if word not in d:
         d[word] = 1
    else:
        d[word] += 1
print(d)
"""counting no words in a string and printing 
with word and count into  a dictionary using inbuilt class"""
d = defaultdict(int)
for word in string_.split():
        d[word] += 1
print(d)

"""counting  words in a string and printing with word and length into  a dictionary"""
string_ = 'not be a state of origin in this context'
d = {}
for word in string_.split():
    d[word] = len(word)
print(d)
"""printing words and its lenth of string (if word is even) into  dictionary 
without using inbuilt methods"""
string_ = 'not be a state of origin in this context'
d = {}
for word in string_.split():
    if len(word) %2 == 0:
        d[word] = len(word)
print(d)

"""printing words and its lenth of string (if word is even) into  dictionary
 (if word starting with vowel)"""
string_ = 'not be a state of origin in this context'
d = {}
for word in string_.split():
    if len(word) %2==0 and word[0].lower() in 'aeiou':
        d[word] = len(word)
print(d)

"""printing words and its count of string into dictionary 
if the word is not repeated  in string"""
string_ = 'this is this of this is'
d = {}
for word in string_.split():
    if string_.count(word)==1:
        d[word] = string_.count(word)
print(d)
"""printing first letter of a word in a string 
as key and that word as list of word (using defaultdict class)"""
string_ = 'This is Mohana Kasi This is'
d = defaultdict(list)
for word in string_.split():
    d[word[0]] += [word]
print(d)