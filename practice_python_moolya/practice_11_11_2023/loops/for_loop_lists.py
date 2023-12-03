'''' traversing through list'''''
list_ = [1,2,3,'kasi']
for item in list_:
    print(item)

for index in range(len(list_)):
    print(list_[index], end=' ')

for index, item in enumerate(list_):
    print(item, index)


"""travesrsing reverse through list"""
list_ = ['laptop', 'pen', 'mobile']
res = []
for item in list_:
    res = [item] +res
print(res)

"""travesrsing reverse through list"""
list_ = ['laptop', 'pen', 'mobile']
for index in range(-1, -(len(list_))-1, -1):
    print(list_[index], end=' ')

""" program to print alternate items in a list (even) """
list_ = ['kasi','nadh',0,12,3]
for index in range(0,len(list_), 2):
    print(list_[index], end=' ')

""" to print alternate items in a list (odd) """
list_ = ['kasi','nadh',0,12,3]
for index in range(1, len(list_), 2):
    print(list_[index], end=' ')
""" program to print only numbers in a list using inbuilt method"""
list_ = ['kasi','jmr',2020]
for item in list_:
    if isinstance(item, (int, float, complex)):
        print(item, end=' ')

""" print item in list with it's length"""
list_ = ['kasi','python','bangalore','2021','2022']
for item in  list_:
    count = 0
    for char in item:
        count += 1
    print(item, count)

for item in list_:
    print(item, len(item))

"""print even length items in a list"""
list_ = ['kasi','python','bangalore','123456','2021','2022']
for item in list_:
    count = 0
    for char in item:
        count += 1
    if count %2 ==0:
        print(item, count)
for item in list_:
    if len(item) %2 == 0:
        print(item, len(item))

"""printing if item in a string is even lenth as is it is , if it is odd length reverse the item
(creating a new lst) """
list_ = ['Hai', 'hello','namaste', 'bangalore', 'python', 'world']
list2_ = []
for item in list_:
    count=0
    for char in item:
        count += 1
    if count %2 == 0:
        list2_ += [item]
    else:
        list2_ += [item[::-1]]
print(list2_)

"""printing if item in a string is even lenth as is it is , if it is odd length reverse the item 
(modifing original list)"""
list_ = ['Hai', 'hello','namaste', 'bangalore', 'python', 'world']
for index, item in enumerate(list_):
    if len(item) %2 ==0:
        continue
    else:
        list_[index] = item[::-1]
print(list_)

"""write a program to modify the exisitng list if item is of type string reverse it else keep it as it is
(modifying original list)"""
list_ = ['kasi','guntur',1008,536,1.85,50+50j,('jmr'),{4253},[85,'mohana'],{'a':52,'b':25200},'python','knows']
for index, item in enumerate(list_):
    if isinstance(item, str):
        list_[index] = item[::-1]
    else:
        list_[index] = item
print(list_)

"""write a program to modify the exisitng list if item is of type string reverse it else keep it as it is
(creating new listlist)"""
list_ = ['kasi','guntur',1008,536,1.85,50+50j,('jmr'),{4253},[85,'mohana'],{'a':52,'b':25200},'python','knows']
list2_ =[]
for index, item in enumerate(list_):
    if isinstance(item, str):
        list2_.append(item[::-1])
    else:
        list2_.append(item)
print(list2_)

"""print the strings in a list which are starting with vowels"""
list_ = ['kasi', 'is', 'from','ernakulam']
for item in list_:
    if item[0].lower() in 'aeiou':
        print(item)

"""wap to print all the extensions in a list"""
list_ = ['youtube.txt','gmail.com','kasi.py','python.exe']
for item in list_:
    exten = item.split('.')[1]
    print(exten, end=' ')

"""wap to print all the file names in a list if file is of odd length"""
list_ = ['youtube.txt','gmail.com','kasi.py','python.exe']
for item in list_:
    exten = item.split('.')[0]
    if len(exten) %2 !=0:
        print(exten, end=' ')

"""wap to print all the file names in a list if file is of odd length (using unpacking)"""
list_ = ['youtube.txt','gmail.com','kasi.py','python.exe']
for item in list_:
    file_name, exten = item.split('.')
    if len(file_name) %2 != 0:
        print(file_name, end=' ')


"""checking index of first occurence of a nimber in list (using inbuilt method)"""
list_ = [20,30,10,50,20,10]
for item in list_:
    print(item, list_.index(item))

"""printing palindrome in a list"""
n = ['kasi','malayalam','dad','mom',8008,1001]
for item in n:
    if str(item) == str(item)[::-1]:
        print(item, 'is a palindrome')
