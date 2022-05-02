import math

#Celem programu jest obliczanie symbolu Newtona z dwóch zmiennych (n,k)
#n - pierwsza zmienna
#k - druga zmienna

n = int(input())
k = int(input())

def symbol_newtona(n,k):
  if k==0 or k==n:
    return 1
  else:
    return n / k * symbol_newtona(n-1, k-1)

print(symbol_newtona(n,k))
