"""printing characters and its count of a string into dictionary uisng inbuilt method count"""
s = 'hello world'
d ={}

for char in s:
    d[char] = s.count(char)
print(d)

"""printing characters and its count of a string into dictionary without using inbuilt method (if - else)"""
s = 'hello world'
d ={}
for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
print(d)

"""printing characters and its count of a string into dictionary using inbuilt class defaultdict"""
from collections import defaultdict
s = 'hello world'
d = defaultdict(int)
for char in s:
    d[char] += 1
print(d)

"""counting no words in a string and printing with word and count into  a dictionary 
using without inbuilt (if-else)"""
s = 'python has python inbuilt modules'
d = {}
for word in s.split():
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

"""counting no words in a string and printing with word and count into  a dictionary using inbuilt method count"""
s = 'python has python inbuilt modules'
words = s.split()
d = {}
for word in words:
    d[word] = words.count(word)
print(d)

"""counting no words in a string and printing with word and count into  a dictionary using inbuilt class"""
from collections import defaultdict
s = 'python has python inbuilt modules'
d = defaultdict(int)
for word in s.split():
    d[word] +=1
print(d)

"""counting  words in a string and printing with word and length into  a dictionary"""
s = 'python has python inbuilt modules'
d = {}
for word in s.split():
    if word not in d:
        count = 0
        for char in word:
            count += 1
        d[word] = count
print(d)

"""printing words and its lenth of string (if word is even) into  dictionary without using inbuilt methods"""
s = 'python has inbuilt modules anid a powerful oops '
d = {}
for word in s.split():
    count = 0
    for char in word:
        count += 1
    if count %2 ==0 and word not in d:
        d[word] = count
print(d)

"""printing words and its lenth of string (if word is even) into  dictionary (if word starting with vowel)"""
s = 'python has inbuilt Eodules anid a powerful oops '
d = {}
for word in s.split():
    count = 0
    for char in word:
        count += 1
    if count %2 == 0 and word[0] in 'aeiouAEIOU':
        d[word] = count
print(d)

"""printing words and its count of string into dictionary if the word is not repeated  in string"""
s = 'python has python inbuilt modules modules anid it has powerful oops '
d = {}
list_ = []
for word in s.split():
    if word not in list_:
        d[word] = 1
        list_.append(word)
print(d)


"""printing first letter of a word in a string as key and that word as list of word (using defaultdict class)"""
from collections import defaultdict
sent = 'hello world welcome to python programmming hi there'
d = defaultdict(list)
for word in sent.split():
    d[word[0]] += [word]
print(d)


"""printing dictionary with items and it's index values of  a list"""
list_ = ['apple','google','gmail','apple']
d = {}
for index, item in enumerate(list_):
    if item not in d:
        d[item] = [index]
    else:
        d[item] += [index]
print(d)

"""swaping keys and values using items method"""
d = {'a': 1, 'b': 2, 'c':3, 'd': 4}
d2 = {}
for key, item in d.items():
    d2[item] = key
print(d2)

"""swaping keys and values using items method"""
d = {'a': 1, 'b': 2, 'c':3, 'd': 4}
d2 = {}
for key, value in d.items():
    d2.update({value:key})
print(d2)

