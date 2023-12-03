"functions"
"inbuilt & userdefined functions"
"return statement"
def asci(char):
    print(ord(char))

asci('H')

def string_rev(string):
    return string[::-1]

print(string_rev('Mohana kasi'))

"types of arguments"
"positional"
def age_spam(name, age):
    print(f"his {name} & {age}")

age_spam('Mohna', 133)


"Keyword arguments"
def spam1(emp_name, loc):
    print(f'Name of the employee {emp_name}')
    print(f"loca of the emp is {loc}")

spam1(emp_name='Kasi', loc='Guntur')


"combination of position & keyword arguments:"
"in this first should come positonal & followed by keyword"
"note: first argument keyword not works"

def sum_nums(a, b, c, d):
    return a+b+c+d

print(sum_nums(10, 20, c=30, d=40))


"only posiotional:"
"in this before / all arguments should be only positonal after / you can take any"
def add_nums(a,b,c,d,/):
    return sum((a,b,c,d))

print(add_nums(10,2,3,5))


"keyword only arguments:"
def add_num(*,a,b,c):
    return sum((a,b,c))

print(add_num(a=10, b=23, c=54))


'Combination of both positional only, keyword only arguments:'
def add_sum(a,b,/,*,c,d):
    return sum((a,b,c,d))

print(add_sum(12,34,c=56,d=67))


"default values"
def prime_check(num, start=2):
    for i in range(start, num):
        if num % i == 0:
            print('Not prime')
            break
    else:
        print('Prime number')

prime_check(100)
prime_check(123)
prime_check(37)

"Variable positional arguments:"
def emp_data(*args):
    return f"emp_name is {args[0]} and emp sal is {args[1]}"

print(emp_data('Mohana kasi', 23432))


"Variable keyword arguments:"
def rev(**kwargs):
    print(kwargs)
    return [item[1] for item in kwargs.items()][0]

print(rev(string_= 'Mohana temp', num=28))


