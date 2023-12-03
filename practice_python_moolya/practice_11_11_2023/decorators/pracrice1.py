
"simple decorator"
import time
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator #say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()


"time decorator to hold a function for few seconds"
def time_deco(func):
    def wrapper(*args, **kwargs):
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper

@time_deco #list_to_deco = time_deco(func)
def list_to_deco(list_):
    dict_ = {}
    new_deco = dict_.fromkeys(list_, 'None')
    print(new_deco)

# list_to_deco(('name', 'lco'))



"count the function how many times it is called"
" and raise value error if it is called more than 5 times"

def count_func_calls(func):
    func.count = 0
    def wraper(*args, **kwargs):
        func.count += 1
        print("welcome to moolya", func.count)
        if func.count >5:
            raise Exception(r"you can not call me more than 5 times, I am going home now")
        return func(*args, **kwargs)
    return wraper

@count_func_calls
def greet_new_emp(actual_msg):
    return actual_msg

print(greet_new_emp('Mohana'))
print(greet_new_emp('kasi'))
print(greet_new_emp('Rao'))
print(greet_new_emp('Viswantath'))
print(greet_new_emp('ram'))
# print(greet_new_emp('melin'))


"""class decorator"""
class String_splitter:

    def __init__(self, func):
        self.func =  func

    def __call__(self, *args, **kwargs):
        # if * in function definition it is packing
        #if * in function call it is unpacking
        print("iam splitting the string into a list of words")
        print(args)
        words = args[0].split()
        self.func(words)


@String_splitter # counting_words = String_splitter(couting_words)
def counting_words(lis_words):
    print(len(lis_words))

counting_words('This is Mohana Kasi')
