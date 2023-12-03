"""
sorted():
•	Returns a new sorted list from the items in the iterable
•	Has two optional arguments which must be specified as keyword arguments
•	Key specifies a function of one argument that is used to extract a comparison key from each element in the iterable. The default value is None
•	Reverse is a Boolean value. If is is true the elements are sorted in reversed order when it is in false the elements are sorted normal

"""
"write a program to sort the elements present in a list based on their length"
list_ = ['Mohana kasi', 'Guntur', 'python coding', 'never regrets']
print(sorted(list_, key=len))

"write a program to find the largest and shortesd word in the following string"
sentence_ = 'python is a high level language'
sor_list = sorted(sentence_.split(), key=len)
print(sor_list)
print(sor_list[0], sor_list[-1])

"write a program to sort the below list elements based on the last character of each string"
list_ = ['python', 'Mohana', 'kasi', 'testing', 'Bangalore']
print(sorted(list_, key=lambda item:item[-1]))


"WAP to sort the below list based on the first character of each element"
list_ = ['python', 'Mohana', 'kasi', 'testing', 'Bangalore']
print(sorted(list_, key=lambda item:item[0]))


"dictionary sorting"


"write a program to sort the dictionary based on the keys last item"
dict_ = {'name': 'Mohana', 'year of birth': 1995, 'age': 27}
print(sorted(dict_, key=lambda item:item[-1]))
print(sorted(dict_.items(), key=lambda item:item[0][-1]))

"write a program to sort the dictionary based on the values"
dict_ = {'name': 'Mohana kasi', 'loc': 'Guntur', 'skill': 'python'}
print(sorted(dict_, key=lambda key:dict_[key]))
print(sorted(dict_.items(), key=lambda item:item[-1]))
print(sorted(dict_.values()))

#WAp to get the most repeated word
sentence_ = 'is having is local you of you is not goog not bad'
words = sentence_.split()
sor_list = sorted(words, key=lambda item:words.count(item))
print(sor_list)
print(sor_list[-1])

#WAP to print longest word with its length
sentence_ = 'python is s high level general purpous programming language'
words = sentence_.split()
print(sorted(words, key=lambda item:len(item))[-1])

