import math

#Celem programu jest obliczanie symbolu Newtona z dwóch zmiennych (n,k)
#n - pierwsza zmienna
#k - druga zmienna

n = int(input())
k = int(input())

if  k==1 or k == n:
    print(1)

if k > n:
    print(0)
else:
    x = math.factorial(n)
    y = math.factorial(k)
    symbolNewtona = x // (y*(n-k))
    print(symbolNewtona)
