""" program to print only numbers in a list using inbuilt method"""
list_ = [1098,'kasi', [1098], 'True']
for item in list_:
    if isinstance(item, int):
        print(item)

""" print item in list with it's length"""
list_ = [1098,'kasi', [1098], 'True']
for item in list_:
    if isinstance(item, str):
        print(item, len(item))
"""print even length items in a list"""
list_ = ['this', 'is', 'Mohana','True']
for item in list_:
    if len(item) %2==0:
        print(item)

"""printing if item in a string is even lenth as is it is , 
if it is odd length reverse the item
(creating a new lst) """
string_ = 'not be the proper evaluation did for the item'
list_ = []
for word in string_.split():
    if len(word) %2 == 0:
        list_.append(word)
    else:
        list_.append(word[::-1])
print(list_)
"""printing if item in a string is even lenth as is it is , 
if it is odd length reverse the item"""
list_ = ['kasi','from','guntur','2021','to','bangalore','2022']
for index, item in enumerate(list_):
    if len(item) %2 == 0:
        list_[index] = item
    else:
        list_[index] = item[::-1]
print(list_)
"""write a program to modify the exisitng list if item
 is of type string reverse it else keep it as it is
(creating new listlist)"""
list_ = ['kasi','guntur',1008,536,1.85,50+50j,('jmr'),{4253},[85,'mohana'],{'a':52,'b':25200},'python','knows']
list2_ =[]
for item in list_:
    if isinstance(item, str):
        list2_.append(item)
    else:
        list2_.append(str(item)[::-1])
print(list2_)
"""print the strings in a list which are starting with vowels"""
list_ = ['kasi', 'is', 'from','ernakulam']
for item in list_:
    if item[0].lower() in 'aeiou':
        print(item)
"""wap to print all the extensions in a list"""
list_ = ['youtube.txt','gmail.com','kasi.py','python.exe']
for item in list_:
    print(item.split('.')[1])
"""wap to print all the file names in a list if file is of odd length"""
list_ = ['youtube.txt', 'gmail.com', 'kasi.py', 'python.exe']
for item in list_:
    if len(item.split('.')[0]) %2 !=0:
        print(item.split('.')[0])

"""wap to print all the file names in a list if file is of odd length (using unpacking)"""
list_ = ['youtube.txt', 'gmail.com', 'kasi.py', 'python.exe']
for item in list_:
    file_name, extension = item.split('.')
    if len(file_name) %2 !=0:
        print(file_name)
# """checking index of first occurence of a nimber in list (using inbuilt method)"""
"""prime number"""
num = 10
for i in range(2, num):
    if i%num == 0:
        print('not a prime')
        break
else:
    print('prime')

"""series of prime numbers"""
n = 10
for num in range(2, n):
    for i in range(2, num):
        if num % i ==0:
            print(num, 'Not a prime number')
            break
    else:
        print(num, 'prime number')
