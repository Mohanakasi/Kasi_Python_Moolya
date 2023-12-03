"recursion intro"
# •	It is a function which call itself until the condition being satisfied
# •	Used to avoid the loop in some cases
# •	Python recursion limit can be found with a function from the sys module called getrecursionlimit()
# •	from sys import getrecursionlimit
# print(getrecursionlimit())
# •	We can change this value by using setrecursionlimit() function
from sys import setrecursionlimit, getrecursionlimit
setrecursionlimit(2500)
print(getrecursionlimit())


"#Write a recursion function to print numbers from 10 to 1"
def nums_print(n):
    if n>0:   #condtion
        print(n, end=' ')
        n-= 1
        return nums_print(n)  #function itself call

# nums_print(10)

"sum of n numbers"
"write a recursive function to find the sum of first n numbers"
def sum_n(n, sum=0):
    if n>0:
        sum += n
        n -= 1
        return  sum_n(n, sum)
    else:
        return sum
# print(sum_n(20))

"counting total digits in a number"
"wrirte a recursive function to count the number of digits in a number"
def count_digits(num, count=0):
    if num>0:
        count += 1
        num//=10 #removes the last character every time
        return count_digits(num, count)
    else:
        return count

# print(count_digits(9856))

"sum of digits in a number"
"wrirte a recursive function to add the digits in a number"
def sum_digits(num, sum=0):
    if num!=0:
        sum += num%10   #get the last digit of a number
        num//=10 #removes last digit every time in the loop
        return sum_digits(num, sum)
    else:
        return sum

# print(sum_digits(345))

"prime number check"
"prime number check using recursive function"
def prime_check(num, start=2):
    if start<num:
        if num % start == 0:
            return "Not prime"
        start += 1
        return prime_check(num, start)
    else:
        return "prime number"

# print(prime_check(37))
# print(prime_check(27))

"series of prime numbers"
def prime_series(n,start=2):
    if n>0:
        def prime_check(i=2):
            if i < start:
                if start % i ==0:
                    print(f"{start} not a prime number")
                    return
                i += 1
                return prime_check(i)
            else:
                print(f"{start} is a prime number")
        prime_check()
        return prime_series(n-1, start+1)
prime_series(30)

"factorial"
def factorial(num, sum=1):
    if num>0:
        sum *= num
        num-= 1
        return factorial(num, sum)
    else:
        return f"factorial of num is {sum}"

# print(factorial(5))
# print(factorial(3))




"fibonaci series"
"printing first 20 fibo numbers"
def fibo_n_nums(n, a=0, b=1):
    if n>0:
        print(a, end=' ')
        c = a+b
        a = b
        b = c
        return fibo_n_nums(n-1, a, b)

# fibo_n_nums(30)
"printing fibonaci series upto the number specified"
def fibo_num_spec(number, a=0, b=1):
    if a<=number:
        print(a, end=' ')
        c = a+b
        a = b
        b = c
        return fibo_num_spec(number, a, b)

# fibo_num_spec(300)
"checking a number is fibo number or not"
def fibo_num_check(number, a= 0, b=1):
    if a<=number:
        if a == number:
            return f"{number}, is a fibo number"
        c = a + b
        a = b
        b = c
        return fibo_num_check(number, a , b)
    else:
        return f"{number} is not a fibo  number"

# print(fibo_num_check(233))
# print(fibo_num_check(300))
"to return nth fibonaci number"
def fibo_nth(n, count=1, a= 0 , b = 1):
    if n==count:
        return f"{a} is {n}th fibo number"

    return fibo_nth(n, count+1, a=b, b= a+b)

# print(fibo_nth(30))
# print(fibo_nth(12))