# #Czy to l. pierwsza

# n = int(input("Podaj liczbę: "))
# if n<=2:
#   print("NIE")
# else:
#   for i in range(2, n):
#     if n % i == 0:
#       print("NIE")
#       break
#   else:
#     print("TAK")



# #pierwsza od jakieś do jakiejś 
# n = int(input()) 
# e = int(input()) 
# for i in range(n,e+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end=" ")


# #do jakiej liczby
# n = int(input("do ilu mam znaleść liczby pierwsze? "))
# for i in range(2,n+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end=" ")




#NWW I NWD

#NWD
# a= int(input())
# b=int(input())
# from math import gcd
# print(gcd(a,b))

# #NWW
# a=int(input())
# b=int(input())
# from math import gcd
# iloczyn=a*b
# NWD=gcd(a,b)
# NWW=iloczyn//NWD
# print(NWW)

# #cezar
# napis=input()
# szyfr=""
# for i in range(len(napis)):
#   szyfr=szyfr+chr(65+ ((ord(napis[i])-65+3) %26))
# print(szyfr)

#RSA 

# 1. Wybór dużych liczb pierwszych
# p = 17
# q = 19
# print(p,q)

# # 2. Obliczenie n=p*q i funkcji Eulera F=(p-1)*(q-1)
# n = p * q
# F = (p - 1) * (q - 1)
# print(n)
# print(F)

# # 3. Generujemy klucz publiczny e taki że, NWD(e,F)=1
# from math import gcd
# for i in range(2,F):
#     if gcd(i,F) == 1:
#         e = i
#         break
# print(e, n)

# # 4. Generujemy klucz prywatny d taki, że (d*e) % F = 1 
# for j in range(2,F):
#     if ((j*e) % F) == 1:
#         d = j
#         break
# print(d,n)





# #Huffman
# W = "AAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCDD"  
# W += "."
# ilosc = 1
# H = ""
# for i in range(len(W)-1):
#   if W[i] == W[i+1]:
#     ilosc += 1
#   else:
#     if ilosc > 1:
#       H += str(ilosc)
#       H += W[i]
#       ilosc = 1
# print(H)


#Ułamki
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# from math import gcd
# x, y = b, d
# iloczyn = x*y
# nwd=gcd(x,y)
# nww=iloczyn//nwd
# e=(nww//b)*a
# f=(nww//d)*c
# g=e+f
# print(f"{g}/{nww}")



# #RSA
# m = input()
# cipher = ""
# for i in m:
#     cipher += chr((ord(i)**e)%n)
# print(cipher)
# tekst=""
# for j in cipher:
#     tekst += chr((ord(j)**d)%n)
# print(tekst)



k = int(input())
suma = 0
for i in range(k):
    x = int(input())
    suma = suma + x
print(suma)
