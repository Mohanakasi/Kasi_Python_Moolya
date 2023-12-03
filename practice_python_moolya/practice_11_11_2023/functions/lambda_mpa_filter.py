#lambda
"""Lambda function:
•	Any anonymous function that defined without name is called as lambda function
•	While in normal functions are defined using the def keyword, anonymous functions are defined using lambda keyword
•	Syntax: lambda [arg1, arg2, arg3……..]: expression
•	after creating lambda function you have to store it in a variable and we have to call that variable by passing arguments
•	in lambda function we can take n number of arguments
•	but expression is only one to take
•	and only one single---->if block is not acceptable in lambda function
•	if we want to take if block in lambda function we have to take else block also
•	we can take and, or logical operators in a single expression
•	pass break continue keywords are not used in lambda function
•	we can take collection (one or any no of) as argument  to the lambda function but expression is one only
•	we can’t do looping in lambda functions
•	to achieve looping we use map and filter functions along with the lambda functions
"""
# lambda variables:expression
add = lambda a,b:a+b
print(add(10, 20))

"write a lambda expression that checks the given no is even or not"
even_check = lambda num:num%2==0
print(even_check(100))
print(even_check(23))

"write a lambda expression that multiplies two numbers"
mul = lambda a,b:a*b
print(mul(10,34))

"write a lambda expression that return last elemts of the sequence"
l_el = lambda sequence:sequence[-1]
print(l_el('Mohana kasi'))
print(l_el(['kasi', 'Mohana'][-1]))

"write a lambda function that checks if the string is palindrome or not"
pal_check = lambda string_:string_==string_[::-1]
print(pal_check('moolya'))
print(pal_check('malayalam'))

"lambda expression to check string is a palindrome and to print it if it is a palindrome"
pal_check = lambda string_: string_ if string_==string_[::-1] else None
print(pal_check('mom'))

"write a lambda express that print's whether the the number is even or odd"
evn_odd = lambda num: "even" if num %2 == 0 else "odd"
print(evn_odd(123))
print(evn_odd(98))

"lambda expression to check string is of even length and string stars with vowel"
temp1 = lambda string_:len(string_) %2 ==0 and string_[0].lower() in 'aeiou'
print(temp1('athe'))


"""map"""
""" 
•   map function applies a function to all the items in the iterable
•	map takes a function and iterable as an arguments
•	in map we can have n no of iterables but the no of iterables must match with the parameters in the function definition
•	if the multiple iterables are of different length data loss will occurs
•	in the function we must use return statement for result
•	if we takes only one if block in function the map will implicitly returns none for the false results
•	after completion of map function we have take it into a variable and type cast it (to list tuple or set only)
"""
#Syntax:  map(function_to_apply, list of inputs)  while mentioning function name no parenthesis needed


"""wap to convert all the strings in the list to upper case using map"""
def upper_conv(string_):
    return string_.upper()

res = map(upper_conv, ['Mohana', 'kasi', 'Python'])
print(list(res))
# print(list(res:= map(upper_conv, ['Mohana', 'kasi', 'python'])))

"""wap to convert all the strings in the list to lower case using map"""
def lower_conv(string_):
    return string_.lower()

res = map(lower_conv, ['MOHANA', 'BANGALORW'])
print(list(res))

"""using lambda"""
res = map(lambda string_:string_.lower(), ['CONVOY', 'KASI', "GUNTUR"])
print(list(res))


"""wap to convert allthe negeative numbers into positive using map"""
list_neg_nums = [-8, -36, -22359]
res = map(lambda num: abs(num), list_neg_nums)
# print(list(res))

"""write a map function that return a list of even numbers inside a list using map"""
list_ = [12, 336, 3, 69]
res = map(lambda num: num if num %2 ==0 else None, list_)
print(list(res))

"""write a map function that takes two lists and return sum of each elements\n"""
"""(sum of first index item of 1ist1   with first index item of list2 .....)"""

res = map(lambda item1, item2:item1+item2, [10, 20, 30], [20, 30, 40])
print(list(res))


'''write a map function that returns lenth of the each string 
present inside the list, tuple, set, and dictionary '''
res = map(lambda string_:len(string_), ['Mohana', 'python', 'jungle'])
print(list(res))

"""using dictionary as an iterable"""
dict_ = {'name': 'Mohana', 'place':'guntur'}
res= map(lambda key: len(dict_[key]), dict_)
print(list(res))


'''write a map function that returns the  numeric data present  
inside the list, tuple, set, and dictionary '''

res = map(lambda item: item if isinstance(item, (int, float, complex)) else None, ['Mohana', 2023, 4+65j, True, False, [1,2,3]])
print(list(res))

"using dictionary"
dict_ = {'name': 'kasi', 'yoj':2023, 'place':4+89j, 'prob+comp':True}
res = map(lambda key: dict_[key] if isinstance(dict_[key], (int, float, complex)) else None, dict_)
print(list(res))

"""write a map function that returns the strings 
having even lenth present inside a list"""
list_ = ['is', 'are','we', 'talling', 'topic']
res = map(lambda string: string if len(string) %2 == 0 else None, list_)
print(list(res))

""""write a map function to create a dictionary 
of word and it's count pair in the following sentence"""
string_ = " is not a normal thing is it more a complexable"
words = string_.split()
res = map(lambda word: (word, words.count(word)), words)
print(dict(res))

""""write a map function to return the words starting with vowels"""
res = map(lambda item: item if item[0].lower() in 'aeiou' else None, ['Mohana', 'is', 'an', 'Enginerr', 'python'])
print(list(res))

""""write a map function to return the palindrome strings inside a list"""
list_ = ['mom', 'dad', '1001', 'kasi', 'Mohana','malayalam']
res = map(lambda item: item if item == item[::-1] else None, list_)
print(list(res))

"""write a map function that returns the list of numbers raised 
to the power of their indices using map"""
"""we cant directly unpack the items in the argument position of lambda function"""
list_ = [1,2,3,4]
# print(list(enumerate(list_)))
res = map(lambda item: item[0]**item[-1], list(enumerate(list_)))
print(list(res))


"""write a map function that returns all the 
words in lower case in the given sentence"""
sentence_ = 'tHIS IS mOHANA kASI'
res = map(lambda word:word.lower(), sentence_.split())
print(list(res))

"""
Filter
•	the filter function takes a function and an iterable as an argument
•	it provides an elegant way to filter out all the elements of a sequence for which the function returns true
•	filter creates a list of elements for which a function returns true
•	filter takes only one iterable as an argument 
•	filter passes each element in the iterable through the function and returns elements which was true
•	if we given any expression after return statement it doesn't execute that
•	Syntax: filter(function, iterable)
"""

"""filter out the even values in the list"""
list_ = [1,23,46,55]
res  = filter(lambda item:item if item%2==0 else None, list_)
print(list(res))

"""write a program that returns a list of strings with odd length using 
filter function"""
list_ = ['Mohana', 'kasi', 'is', 'from', 'python', 'batch']
res = filter(lambda item:item if len(item) %2 !=0 else None, list_)
print(list(res))

'''write a function that returns only the  numeric data present 
 inside the list, tuple, set, and dictionary '''

list_ = ['kasi', 2023, True, [1,2,3], 2+45j, {1,2,3}]
res = filter(lambda item: item if isinstance(item, (int, float, complex)) else None, list_)
print(list(res))

