#zad 1
a = int(input())
b = int(input())
if (a + b) % 2==0:
  print ("Yes")
else
  print ("No")

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
  print ("tak")
  print(k, l)
  
if l==m:
  print("tak")
  print(l, m)

if m==k:
  print ("tak")
  print (m, k)

#zad 5
a = int(input())
b = int(input())
c = int(input())
if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
   print("tak")
else:
  print("nie")