import math

x = str(input())
x = x.split(' ')
liczby = [int(i) for  i in x]

n = liczby[0]
k = liczby[1]

if k == 1 or k == n:
    print(1)

if k > n:
    print(0)
else:
    x = math.factorial(n)
    y = math.factorial(k)
    z = math.factorial(n-k)
    symbolNewtona = x // (y*z)
    print(symbolNewtona)
