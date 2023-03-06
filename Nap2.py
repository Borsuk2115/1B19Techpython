# # palidrom za pomocą tablic

# s = input()
# for i in range(len[s]//2):
#   if s[i] != s[len(s)-1-i]:
#     exit("Nie jest palidromem")
# exit("Jest palidromem")



# anagram za pomocątablic

#Sobosób I za pomocą funkcji

a = input()
b = input()

A = list(a)
B = list(b)

A.sort()
B.sort()

a= " ".join(A)
b= " ".join(B)
print(a, b)
if a==b:
  print("Tak")
else:
  print("Nie")