''"""print list having powers of each element of another list"""''
"""(normal method)"""
list_ = [1,2,3,4]
res = []
for item in list_:
    res.append(item**2)
print(res)

"list comprehension"
print(res := [item**2 for item in list_])

"""to print a list having tuple of index and item of another list normal method"""
"""(normal method)"""
list_ = [1,2,3,4]
res  = []
for index, item in enumerate(list_):
    res.append((index, item))
print(res)

"using list comprehension"
print(res:=[(index, item) for index, item in enumerate(list_)])

"""creating list of even no's using list comprehension"""
print(res:=[item for item in list_ if item %2 == 0])

"""creating lists of even and odd using list comprehension"""
list_ = list(range(1,20))
print(res:=[item for item in list_ if item %2 == 0])
print(res:=[item for item in list_ if item %2 != 0])

"""   if word is of even append into list as it is if word lenth is odd reverser it """
"""(using normal method)"""
list_ = ['kasi' , 'jmr', 'mohana' , '123']
res = []

for word in list_:
    if len(word) %2 == 0:
        res.append(word)
    else:
        res.append(word[::-1])
print(res)

"using list compreshension"
print(res:=[word if len(word) %2 == 0 else word[::-1] for word in list_])


"""if item in a list is string keep it as it is else reverse that item"""
list_ = ['kais',1.0,True,[1,4,56]]
print(res:=[item if isinstance(item, str) else str(item)[::-1] for item in list_])

"""create a list having words starting with owel (using list comprehension)"""
list_ = ['kasi', 'User', 'Imr','iam']
print(res:=[item for item in list_ if item[0].lower() in 'aeiou'])


"""wap to reverse the elements in the list using list comprehension"""
list_ = ['kasi','python',1008,'happy']
print(res:=[item for item in list_[::-1]])

"""wap to preint alternate elements (even)"""
list_ = ['python',1.58,True,'kasi','laguage0']
print(res:=[list_[index] for index in range(0, len(list_), 2)])

"""wap to print alternate elements (odd)"""
list_ = ['python',1.58,True,'kasi','laguage0','kil']
print(res:=[list_[index] for index in range(1, len(list_), 2)])


"""wap to print only integers in a list"""
list_ = ['kasi', 2021 , 'python' , 1008, 50200037008003 , 'test yanthra', 2022]
print(res:=[item for item in list_ if isinstance(item, (int, float, complex))])

"""wap to print iterable with it's length"""
list_ = ['kasi','python', [1,2,3,'kasi'],{458,25,'a'},{'a':1,'b':1},('py','by'),True,1.8,10087]
print(res:=[(item, len(item)) for item in list_ if isinstance(item, (str, list, tuple, set, dict))])

"""wap to print strings in list which are of even length"""
list_ = ['mohan','kasi','is','a','king','before','guntur','minister']
print(res:=[item for item in list_ if len(item) %2 == 0])

"""wap to print strings in the list if the string is of even lenth keepit as it is if it is odd lenth reverse it"""
list_ = ['kasi','python', 'has','00a','inbuilt','modules','and','oops']
print(res:=[item if len(item) %2 == 0 else item[::-1] for item in list_])

"""wap to reverse the element if it is of type string elser keep it as it is (using list comprehension)"""
list_ = ['kasi',True,1008,False,2021,'python','jmr',[1,4,0,80]]
print(res:=[item[::-1] if isinstance(item, str) else item for item in list_])

"""wap to print all the palindrome in a list"""
list_ = ['mom','is','better','then','malayalam','dad']
print(res:=[item for item in list_ if item == item[::-1]])
