# 1.napisz algorytm który wypisze wszystkie dzielniki liczb od 23-28
# for i in range(23,29):
#   print(i)
#   for j in range(1,i+1):
#     if (i%j==0):
#       print(j,end=" ")
#   print()
# 2.napisz algorytm który narysuje to:
#   *
#  ***
# *****
# ilość linijek zależy od liczby którą poda użytkownik przykład pokazuje 3
ilosclinijek = int(input())
srodek=ilosclinijek-1
for i in range(ilosclinijek):
  for j in range(ilosclinijek*2):
    if(j>=srodek-i and j<=srodek+i):
      print("*",end="")
    else:
      print(" ",end="")
  print()
# 3.napisz algorytm który obliczy śrędnią liczb podanych przez użytkownika (ilość liczb 
# wybiera użytkownik i wynik musi mieć liczby po przecinku)
# a = int(input())
# b = 0
# w = 0
# for i in range(a):
#   b = int(input())
#   w = w + b
# print(w/a)