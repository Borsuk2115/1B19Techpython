#zad  2 
# n= int(input())
# for i in range(1,n+1):
#     print("*"i*, end= " ")
#   if i %2 == 0:
#     print("--", end+" ")
#   else:
#     print("||", end=" ")
    

#zad 7
# int n = int(input())

# for i in range(n):
#   for j in range(n):
#     print(f{i},{j})", end=" ")


n= int(input())
for i in range(2, n):
  if n % i == 0:
    print("Liczba nie jest pierwsza")
    exit(0)
    print("Liczba jest pierwsza")