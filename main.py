import math

n = int(input())
k = int(input())

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

