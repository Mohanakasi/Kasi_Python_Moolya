''"""traversing through set"""''
set_ = {'kasi',1008,1,2,3}
for key in set_:
    print(key, end=' ')

"""removing a particular element in a set"""
set_ = {1,2,3,4}
value = 3
# for key in set_:
#     if key == value:
#
set_.remove(value)
print(set_)

""" remove the element from the set  """

set_ = {"python", "dad", "hai", "malayalam", "madam", "mom"}
value = "hai"
for key in set_:
    if key == value:
        set_.remove(key)
        break
print(set_)

"""adding items into a set  if the  item is a palindrome"""
list_ = ['kasi','malayalam','dad','mom']
set_= set()
for item in list_:
    if item == item[::-1]:
        set_.add(item)
print(set_)


"zip class"
s1 = 'Hai'
s2 = 'Hel'
s3 = 'Hmm'
for item1, item2, item3 in zip(s1, s2, s3):
    print(item1, item2, item3)

"if the items are not in unique lengths we need to use zip_longest"
from itertools import zip_longest
s1 = 'hai'
s2 = 'hello'
for item in zip_longest(s1, s2, fillvalue='Not present'):
    print(item)


