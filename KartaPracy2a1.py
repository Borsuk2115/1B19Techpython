 #zad 1
a = int(input())
 b = int(input())
 if (a+b) % 2 == 0:
   print("tak")
 else:
   print("nie")

 #zad 2
 import math
 a = int(input())
 g = int(input())
 if (a+g)/2 > math.sqrt(a*g):
   print("tak")
 else:
   print("nie")

 #zad 3
 k = int(input())
 l = int(input())
 m = int(input())
 if k==l:
   print("tak")
   print(k, l)

 elif l==m:
   print("tak")
   print(l, m)

 elif m==k:
   print("tak")
   print(m, k)
 else:
   print("nie")

 #zad 4
 a = int(input())
 b = int(input())
 c = int(input())
 d = int(input())
 print(min(a, b, c, d)) 

 #zad 6
 a = int(input())
 b = int(input())
 c = int(input())
 if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
  if a**2 + b**2 == c**2 :
   print("trókąt prostokątny")

  elif a**2 + b**2 < c**2 :
   print("trójkąt rozwartokątny")

  elif a**2 + b**2 > c**2 :
   print("trójkąt ostrokątny")

 else:
   print("nie")