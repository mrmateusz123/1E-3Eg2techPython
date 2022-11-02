# zad 1
# n=int(input())
# for i in range(n):
#   print("x-|")
# zad 2
# n=int(input())
# for i in range(1,n+1):
#  print("*"*i,end="")
#  if i%2:
#    print("||",end="")
#  else:
#    print("--",end="")
# zad 3
# n=int(input())
# for i in range(1,n+1):
#  if i%2==0:
#    print("-"*i, end="")
#  else:
#   print("*","|"*i,"*", end="")
# Pre
# for i in range(1,11):
#   for j in range(1,11):
#     print(i*j,end="\t")
#   print()
n=int(input("test:"))
# for i in range(n+1):
#   print("*"*i,end="")
#   print(" ")
# for i in range(n+1):
#   print("*"*(n-i-1),end="")
#   print(" ")
# for i2 in range(n):
#   for j in range(i2+1):
#     print("*",end="")
#   print()
# print()
# for i3 in range(n):
#   for j3 in range(n-i3):
#     print("*",end="")
#   print()
# print()
# print()
# for i4 in range(n):
#   for j4 in range(n-i4-1):
#     print(" ",end="")
#   for k4 in range(n-i4-1,n):
#     print("*",end="")
#   print()
# print()
# for i5 in range(n):
#   for j5 in range(i5):
#     print(" ",end="")
#   for k5 in range(i5,n):
#     print("*",end="")
#   print()
# print()
for i in range(n):
  for j in range(n):
    if i>=j:
      print("*",end="")
    else:
      print(" ",end="")
  print()
print()
for i in range(n):
  for j in range(n):
    if j>=i:
      print("*",end="")
    else:
      print(" ",end="")
  print()
print()
for i in range(n):
  for j in range(n):
    if j==i:
      print("*",end="")
    else:
      print(" ",end="")
  print()
print()
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      print("*",end="")
    else:
      print(" ",end="")
  print()  
for i in range(n):
  for j in range(n):
    if i>j:
      print(" ",end="")
    else:
      print("*",end="")
  print()
for i in range(n):
  for j in range(n):
    if i<=j:
      print("*",end="")
    else:
      print(" ",end="")
  print()