# # #PRE

# # from math import gcd
# # print(gcd(20,15))

# # #Wybór dużych liczb pierwszych
# # p= 11
# # q= 13
# # print(p,q)
# # #2 obliczanien=p*q i funkcji Eulera (f- p-1)*(q-1)

# # n = p * q 
# # F= (p- 1) * (q-1)
# # print(n)
# # print(F)


# #4 generujemy klucz prywatny dtaki że (d*e) % F=1
# for j in range(2,F):
#   if ((j*e) % F) == 1:
#     d = j
#     break
# print(d,n)
