# # a= int(input())
# # b= int(input())
# # while a != b:
# #   if a > b : a = a - b
# #   elif b > a : b- a
# # print(a)


# a= int(input())
# b= int(inpput())

# while b > 0:



  #zadanie nww

a = int(input())
b = int(input())
iloczyn = a * b
while a != b:
  if a > b : a = a - b
  elif b > a : b - a
NWD = a

print(iloczyn // NWD)

#to samo tylko modulo
a = int(input())
b = int(input())
iloczyn = a * b
while b > 0:
  a, b = b, a%b
  print(a)
  