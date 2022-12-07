# 2.napisz algorytm który narysuje to:
#   *
#  ***
# *****
# ilość linijek zależy od liczby którą poda użytkownik przykład pokazuje 3
# a = int(input())
# for i in range(1,a+1):
#   for j in range(1,a+1):
#     print(i,end=".")
#     print(j,end=" ")
#   print()
# 1.1 1.2 1.3 1.4 1.5
# 2.1 2.2
# ilosclinijek = int(input())
# srodek=ilosclinijek-1
# for i in range(ilosclinijek):
#   for j in range(ilosclinijek*2):
#     if(j>=srodek-i and j<=srodek+i):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()