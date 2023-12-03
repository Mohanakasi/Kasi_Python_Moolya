#example1:  Treating the functions as objects.
# def temp1(string):
#     return string.split()
#
# print(temp1('Kasi from guntur'))
# f1 = temp1
# print(f1('Mohana kasi'))


#example2: Passing the function as an argument
def rev_string(string_):
    return string_[::-1]

def string_split(string_):
    return string_.split()

def greet(func):
    print(f"{func.__name__}  iam called by {greet.__name__}")
    print(func('This is sample data for decorators'))

greet(rev_string)
greet(string_split)



#example3: returning function from another
def greeting(greet_msg):
    def msg_convy(actual_msg):
        return greet_msg+actual_msg

    return msg_convy
temp1 = greeting('Welcome to moolya')
print(temp1('Mohana kasi'))



