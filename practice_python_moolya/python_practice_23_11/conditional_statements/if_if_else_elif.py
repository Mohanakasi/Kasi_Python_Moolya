""" WAP to check if the given input number is even or odd"""
num = 198
if num%2==0:
    print(num, 'is a even')
""" WAP to check if the character is lowercase or uppercase"""
char_ = 'a'
if 'a'<=char_<='z':
    print(char_ , 'is in lower')


"""checking the element is present in tupple"""
'''checking if character is a alphabet or number or special character'''
char_ = '0'
if 'a'<=char_<='z' or 'A'<=char_<='Z':
    print('alphabet')
elif '0'<=char_<='9':
    print('number')
else:
    print('special character')


'''chech wheter iterable is empty or not'''
list_ = []
if list_:
    print('Not empty')
else:
    print("Empty")
'''converting character to lower and lowe to upper'''
char_ = 'l'
if 65<=ord(char_)<=90:
    # print(ord(char_))
    print(chr(ord(char_)+32))
elif 97<=ord(char_)<=122:
    # print(ord(char_))
    print(chr(ord(char_)-32))

'''converting character to lower and lowe to upper only using inbuilt methods'''
char_ = 'P'
if 'a'<=char_<='z':
    print(char_.upper())
elif 'A'<=char_<='Z':
    print(char_.lower())

'''checking string starts with vowel'''
string_ = 'I am kasi'
if string_[0].lower() in 'aeiou':
    print('starts with vowel')
'''checking string ends with vowel'''
string_ = 'I am kasi'
if string_[-1].lower() in 'aeiou':
    print('ends with vowel')

'''checking integer is palindrome'''
num = 1001
if str(num)[::-1] == str(num):
    print('palindrome')
'''checking iterable contains even or odd no of elements'''
list_ = [1,2,3,4,5]
if len(list_) % 2 !=0:
    print("contains odd no of elements")


'''checking if the number has first digit as even or odd'''
num = 49967
if int(str(num)[0]) %2 == 0:
    print('even')
else:
    print('odd')

'''checking if the number has first digit as even or odd (using inline if- else)'''
print('even'  if int(str(num)[0]) %2 == 0 else 'odd')

