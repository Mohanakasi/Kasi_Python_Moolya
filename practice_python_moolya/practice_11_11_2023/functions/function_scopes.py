"""
Global variable:
•	A variable created in global name space i.e outside a function
•	It can be accessed inside a function but can’t be modified
•	In order to modify a global variable inside a function then we need to use global keyword
"""

"accessing gloabal variable inside a function"
age = 28
def info(name):
    print(f'the candidate name is {name} & age is {age}')

info('Mohana')

"accessing and modifying global variable inside a function"
age = 27
def info_age(name):
    global age
    age += 1
    print(f'the candidate name is {name} & age is {age}')

info_age('kasi')


"""Local variable():
•	A variable which is created inside a function is called local variable and it cant be accessed outside the function
"""

def temp(a, b):
    c = a+b #here c is a local variable
    print(c)

temp(10, 100)
# print(c) --> gives the error



"""
Non local scopes:
•	Non local scopes are those which are neither local or global
•	If a nested function has to modifies the variable of outer function, non local keyword should be used
"""

def outer(a, b):
    c = a+b
    print(c)
    def inner():
        nonlocal c
        c += 100 #c is a non local variable need to define with non local keyword
        print(c)
    inner()

outer(10,20)



