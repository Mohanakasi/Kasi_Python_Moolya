#WAP to check whether the user input number is even or not
# num = int(input("Enter the number"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

#WAP to check the given chracter is in lower case or not
# char = input("Enter the character")
# if 97<=ord(char)<=122:
#     print(char, 'is in lower case')
# else:
#     print(char, 'is in upper case')

#write a program to check whether given element is present in collection or not
elem = 'i'
if elem in 'Mohana kasi':
    print('present')
else:
    print('Not present')

#WAP to check given iterable is empty or not
iterable_ = ['kasi']
if iterable_:
    print('Not empty')
else:
    print('Empty')

#WAP to convert lowe case letters into upper and upper to lower
char_ = 'e'
if 97<=ord(char_)<=122:
    print(chr(ord(char_)-32))
elif 65<=ord(char_)<=90:
    print(chr(ord(char_)+32))


#WAP to check the string is starting with vowel or not
string_ = 'is Mohana Kasi'
if string_[0] in 'aeiouAEIOU':
    print("starts with vowel")
else:
    print("Not starts with vowel")

#WAP to check the string is ending with vowel or not
string_ = 'is Mohana Kasi'
if string_[-1] in 'aeiouAEIOU':
    print("Ends with vowel")
else:
    print("Not ends with vowel")

#WAP to check whether string is palindrome or not
string_ = '1001'
if string_ == string_[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')

#WAP to check whether integer is a palindrome or not
num = 1009
if str(num) == str(num)[::-1]:
    print('Palidromme')
else:
    print('Not a palindrome')

#WAP to check whether the iterable has even number of elements or not
list1 = [1, 'kasi', 1985, True]
if len(list1) %2 == 0:
    print('has even no of elmes')
else:
    print('not having even no of elems')

#WAP to  check if the first digit of the given number is odd or not
num = 429320
if int(str(num)[0]) %2 == 0:
    print('Even')
else:
    print('odd')

"inline if else"
print("Even" if int(str(num)[0]) %2 == 0 else "odd")


