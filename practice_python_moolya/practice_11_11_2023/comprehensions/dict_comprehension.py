""" WAP to create a dictionary with item and its index pair"""

"""normal method"""
string_ = "hello"
res = {}
for index, char in enumerate(string_):
    res[char] = index
print(res)

print(res:={item:index for index, item in enumerate(string_)})

""" WAP to create a dictionary with word and its length pair"""
"""normal method"""
string_ = 'kasi nadh'
dict_ = {}
for word in string_.split():
    dict_[word] = len(word)
print(dict_)
print(res:={word:len(word) for word in string_.split()})


"""word and it's count pair"""
from collections import defaultdict
dict_ = defaultdict(int)
s = 'kasi nadh is a king of kasi palace'
for word in s.split():
    dict_[word] += 1
print(dict_)

s = 'kasi nadh is a king of kasi palace'
print(res:={word:s.split().count(word) for word in s.split()})

"""printing dictionaryu with word and its count pair only if word is of even length"""
s = 'kasi nadh is a king of kasi palace'
dict_ = defaultdict(int)
for word in s.split():
    if len(word) %2 == 0:
        dict_[word] += 1
print(dict_)

print(res:={word:s.split().count(word) for word in s.split() if len(word) %2 == 0})

""" take key as index and words as values if the word in a string is of odd lenth reverse it else keep as iti is"""
s = 'kasi nadh is a king of kasi palace hotstar'
print(res:={index:word if len(word) %2 == 0 else word[::-1] for index, word in enumerate(s.split())})

"""(creating a dictionary with word and it's length psir if word is starting with vowel)"""
s = 'kasi nadh is a king of kasi palace'
print(res:={word:len(word) for word in s.split() if word[0].lower() in 'aeiou'})


"""to create a dictionary with index and item pair if the item is o string data type reverse it 
else keep it as it is"""
list_ = ['kasi',108,True,'nadh']
print(res:={index:item[::-1] if isinstance(item, str) else item for index, item in enumerate(list_)})


"""to create a dictionary with item and index pair if the item is o string data type keep it as it is 
else reverse it"""
list_ = ['mohana','kasi','jmr',1008,50+50J,True]
print(res:={index:item if isinstance(item , str) else str(item)[::-1] for index, item in enumerate(list_)})

"""swaping keys and values"""
d  = {'a':1,"b":2,'c':30}
print(res:={d[key]:key for key in d})
print(res:={value:key for key, value in d.items()})

""" char and ascii value pair """
string = "python"
print(res:={char:ord(char) for char in string})




