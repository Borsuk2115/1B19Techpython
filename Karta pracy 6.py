#zad 1

# a= int(input())
# b= int(input())
# c= int(input())
# if b - a == c - b:
#   print("ciąg jest aretmetyczny")
# if b//a == c//b:
#   print("ciąg jest geometryczny")
# if a<b and b<c:
#   print("rosnący")
# if a>b and b>c:
#   print("malejący")

#zad 2
# suma= 0:
# for i in range(100, 1000):

#   if i%8==0 and i%16!= 0:
#     suma +=i
# print(suma)

#zad 4
ilość = 0
for i in range(10, 100):
  cd =i //10
  cj = i% 10
  if cd >= 2*cj:
    ilość += 1
    print(ilość)