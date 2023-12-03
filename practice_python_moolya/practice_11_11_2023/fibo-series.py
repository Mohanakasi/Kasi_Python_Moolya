
"fibonaci series"
"printing first 20 fibo numbers"
n = 20
i = 0
a = 0
b = 1 #helping varible only
while i<=n:
    print(a, end=' ')
    c = a+b
    a = b
    b = c
    i += 1

"printing fibonaci series upto the number specified"
n  = 100
a  = 0
b = 1
while a<=n:
    print(a, end=' ')
    c = a+b
    a  = b
    b = c

"checking a number is fibo number or not"
num = 35
a = 0
b = 1
while  a<=num:
    if a == num:
        print(num, 'is a fibo num')
        break
    else:
        c = a+b
        a = b
        b = c
else:
    print(num, 'is not a fibo num')


"to return nth fibonaci number"
n = 10
i = 1
a = 0
b = 1
while i<=n:
    if i==n:
        print(a)
        break
    else:
        c = a+b
        a = b
        b = c
        i += 1

