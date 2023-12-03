"#Write a recursion function to print numbers from 10 to 1"
def nums_print(n):
    if n>0:
        print(n, end=' ')
        return nums_print(n-1)
nums_print(10)
print()
"sum of n numbers"
"write a recursive function to find the sum of first n numbers"
def sum_n(n, sum=0):
    if n>0:
        sum += n
        return sum_n(n-1, sum)
    return sum

print(sum_n(3))
"counting total digits in a number"
"wrirte a recursive function to count the number of digits in a number"
def count_digi_num(number, count=0):
    if number>0:
        count += 1
        number//=10
        return  count_digi_num(number, count)
    return count

print(count_digi_num(2567))
"sum of digits in a number"
"wrirte a recursive function to add the digits in a number"
def sum_digi_num(number, count=0):
    if number>0:
        count += number % 10
        number//=10
        return  sum_digi_num(number, count)
    return count

print(sum_digi_num(2567))
"prime number check"
"prime number check using recursive function"
def prime_check(number, start=2):
    if start<number:
        if number % start == 0:
            return f"{number}  not a prime number"
        return prime_check(number, start+1)
    else:
        return f"{number} is a prime number"
print(prime_check(6))
"series of prime numbers"
def prime_series(n, number=2):
    if number<=n:
        def prime_check(number, start=2):
            if start<number:
                if number % start == 0:
                    print(f"{number} is not a prime number")
                    return
                return prime_check(number, start+1)
            else:
                print(f"{number} is a prime number")
        prime_check(number)
        return prime_series(n, number+1)
# prime_series(100)
"factorial"
def factorial(num, fact=1):
    if num>0:
        fact = fact * num
        num -=1
        return factorial(num, fact)
    else:
        return fact
print(factorial(10))
"fibonaci series"
"printing first 20 fibo numbers"
def fibo_n(n, a = 0, b=1):
    if n>0:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        return fibo_n(n-1,  a, b)

fibo_n(20)

"printing fibonaci series upto the number specified"
def fibo_up_to_num(number, a=0, b=1):
    if a<=number:
        print(a, end=' ')
        c = a+b
        a = b
        b = c
        return fibo_up_to_num(number, a, b)

fibo_up_to_num(500)
print()
"checking a number is fibo number or not"
def fibo_check_num(number, a=0, b=1):
    if a<=number:
        if a == number:
            return f"{number} is a fibo number"
        else:
            c = a+b
            a = b
            b = c
            return fibo_check_num(number, a, b)
    else:
        return f"{number} is not a fibo number"
print(fibo_check_num(number=1597))
"to return nth fibonaci number"
def nth_fibo_num(n, i=0, a=0, b=1):
    if i<=n:
        if i == n:
            print(a, f'is {n}th fibo number')
        else:
            c = a+b
            a = b
            b = c
            return nth_fibo_num(n, i+1, a, b)

nth_fibo_num(30)
