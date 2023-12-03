# import calendar
# year = 2020
# month = 12
# print(calendar.month(year, month))


#print natural numbers from 1 to 30
i = 1
n = 30
while i<=n:
    print(i, end=' ')
    i += 1

#check a number is a prime number or not
# num = 13
# for i in range(2, num):
#     if num % i == 0:
#         print('Not a prime number')
#         break
# else:
#     print('Prime number')


#print series of prime numbers
for num in range(2, 31):
    for i in range(2, num):
        if num % i == 0:
            print(num, 'is a prime number')
            break
    else:
        print(num, 'Not a prime number')

#Python Program to Count Occurrence of a Character
string_ = 'Hello Hi'
i = 0
char = 'H'
count = 0
while i<=len(string_)-1:
    if char == string_[i]:
        count += 1
    i += 1
print(count)
#Python Program to Count Total Characters in a String using while loop
string_ = 'This is Mohana kasi'
i = 0
count = 0
while i<=len(string_) -1:
    count += 1
    i += 1
print(count)

#Python program to Count Total Number of Words in a String
string_ = 'This is Mohana kasi'
i = 0
count = 1
while i<=len(string_)-1:
    if (string_[i] == ' ' or string_ == '\n' or string_ == '\t'):
        count += 1
    i += 1
print(count)

#Python Program to Count Vowels in a String
string_ = 'This is Mohana kasi'
i = 0
count = 0
while i<=len(string_)-1:
    if string_[i] in 'aeiouAEIOU':
        count +=1
    i +=1
print(count)



#Python Program to Check If Two Strings are Anagram
"the strings having same type of charcters in it"
str1 = 'triangle'
str2 = 'integral'
if (sorted(str1) == sorted(str2)):
    print(True)
else:
    print(False)

#Python Program to Replace Blank Space with Hyphen in a String
str1 = 'This is Mohana kasi'
str2 = ''
i = 0
while i<=len(str1)-1:
    if str1[i] == ' ':
        str2+= '-'
    else:
        str2 += str1[i]
    i += 1
print(str2)


#Python Program to Reverse String
str1 = 'Python is a language'
i = 0
str2 = ''
while i<=len(str1)-1:
    str2 = str1[i]+ str2
    i +=1
print(str2)

for char in str1:
    str2 = char + str2
print(str2)


#lists
#Python Program to Append an Item to a List
list_ = [1, 9,'kasi']
list_.append('Mohana')
print(list_)
list_ = list_+['jmr']
print(list_)

#Python Program to access List Index and Values
list_ = ['kasi', 1098, 'guntur']
# for index, value in enumerate(list_):
#     print(index, value, end=' ')

#Python Program to Count Even and Odd Numbers in a List
list_ = [1, 9, 23, 567, 4]
count_even = 0
count_odd = 0
for item in list_:
    if item %2 == 0:
        count_even +=1
    else:
        count_odd += 1
print(count_even, count_odd)

i = 0
count_even = 0
count_odd = 0
while i<len(list_)-1:
    if list_[i] %2 ==0:
        count_even += 1
    else:
        count_odd += 1
    i += 1

print(count_even, count_odd)

#Python Program to Print Positive Numbers in a List
list_ = [1, -98, 76]
for item in list_:
    if item>0:
        print(item)

i = 0
while i<=len(list_)-1:
    if list_[i] > 0:
        print(list_[i])
    i += 1

#Python Program to find Second Largest Number in a List
list_ = [1, 53, 2, 45, 22]
list_.sort()
print(list_[-1])
print(list_[-2]) #second largest


