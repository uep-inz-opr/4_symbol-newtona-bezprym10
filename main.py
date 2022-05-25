import math

#Celem programu jest obliczanie symbolu Newtona z dwóch zmiennych (n,k)
#n - pierwsza zmienna
#k - druga zmienna

n = int(input("Podaj liczbę n (w liczniku): "))
k = int(input("Podaj liczbę k (w mianowniku): "))

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

