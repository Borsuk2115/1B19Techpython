#funkca ord()-zwraca kod ASCII znaku

# print(ord("A"))
# print(ord("Z"))
# # w Python kody ASCII wielkich liter A-Z są od 65-90


# #funkcja chr()- zwraca znak dla danego kodu 
# print(chr(66))
# print(chr(75))

#zadanie testowe wypisz alfabet wielkich liter

# for i in range(65, 91):
#   print(chr(i), end=" ")



# sring w python- "lista" 

napis = "KOT"
szyfr = ""
# print(napis[0], napis[1], napis[2])
for i in range(len(napis)):
  print(napis[i])
  szyfr = szyfr + chr(ord(napis[i])+3)
  print(szyfr)
  