#Wczytaj dowolny napis i wpisz z niego pierwsza i ostatnią all

# x = input()
# print(x[0], x[-1])

#zad 5 Policz ile we wpisanym napisie jest liter A


a=input()
ilosc = 0
for x in a:
  if x == "A":
    ilosc = ilosc + 1
print(ilosc)
    