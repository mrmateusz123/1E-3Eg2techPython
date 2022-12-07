# Zad 1
# a=int(input("podaj liczbe a:"))
# b=int(input("podaj liczbe b:"))
# if ((a+b)%2==0):
#  print("Tak")
# else:
#  print("Nie")
# Zad 2
# a=int(input("podaj liczbe a:"))
# g=int(input("podaj liczbe g:"))
# import math
# if (((a+g)/2)>(math.sqrt(a*g))):
#  print("Tak")
# else:
#  print("Nie")
# Zad 3
# k=int(input("podaj liczbe całkowitą k:"))
# l=int(input("podaj liczbe całkowitą l:"))
# m=int(input("podaj liczbe całkowitą m:"))
# if (k==l and l==m):
#   print("Są 3 takie same",m)
# else:
#  if (k==l):
#   print("Tak",k)
#  else:
#    if (k==m):
#     print("Tak",k)
#    else:
#     if (m==l):
#      print("Tak",m)
#     else:
#       print("Nie ma 2 takich samych liczb")
# Zad 4
# a=int(input("podaj liczbe całkowitą a:"))
# b=int(input("podaj liczbe całkowitą b:"))
# c=int(input("podaj liczbe całkowitą c:"))
# d=int(input("podaj liczbe całkowitą d:"))
# w=0
# if (a<=b and a<=c and a<=d):
#  w=a
# if (b<=a and b<=c and b<=d):
#  w=b
# if (c<=a and c<=b and c<=d):
#  w=c
# if (d<=a and d<=b and d<=c):
#  w=d
# print("najmniejsza liczba to",w)
# Zad 5
# a=int(input("podaj liczbe a:"))
# b=int(input("podaj liczbe b:"))
# c=int(input("podaj liczbe c:"))
# if (a+b>c and b+c>a and a+c>b):
#  print("Tak")
# else:
#  print("Nie")
# Zad 6
# a=int(input("podaj bok a:"))
# b=int(input("podaj bok b:"))
# c=int(input("podaj bok c:"))
# n=0
# m=0
# if (a==b or b==c or a==c):
#  if (a==b and b==c):
#    print("trójkąt ostrokątny")
#  if (a==b):
#    if(a>c):
#      print("trójkąt ostrokątny")
#    else:
#      print("trójkąt rozwartokątny")
#  if (a==c):
#    if(a>b):
#      print("trójkąt ostrokątny")
#    else:
#     print("trójkąt rozwartokątny")
#  if(c==b):
#    if(b>a):
#      print("trójkąt ostrokątny")
#    else:
#      print("trójkąt rozwartokątny")
# else:
#  if (a>b and a>c):
#   n=a*a
#   m=b*b+c*c
#  if (b>c and b>c):
#   n=b*b
#   m=a*a+c*c
#  if (c>a and c>b):
#   n=c*c
#   m=b*b+a*a
#  if (m==n):
#   print("Trójkąt prostokątny")
#  if (m>n):
#   print("Trójkąt ostrokątny")
#  if (m<n):
#   print("Trójkąt rozwartokątny")