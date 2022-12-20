# n = int(input())
# for i in range(n):
#   print("∗−|",end="")
# n = int(input())
# for i in range(n):
#   t=i+1
#   if(i%2==0):
#     print("*"*t,end="||")
#   else:
#     print("*"*t,end="--"*t)
# ∗|| ∗ ∗ − − ∗ ∗ ∗ || ∗ ∗ ∗ ∗ − −..
# n = int(input())
# for i in range(1,n+1):
#   if(i%2==1):
#     print("*",end="|"*i)
#   else:
#     print("*",end="-"*i)
# ∗| ∗ − − ∗||| ∗ − − − − ∗|||||..
# 2a
# 3b
# z8
W = float(input("Podaj kwotę wejściową: "))
L = float(input("Podaj okres inwestycji w latach: "))
t=1
t1=0
for i in range(1, int(L*2+1)):
  if(t==1):
    t1 = ((W * 1.06) - W) / 2
    t=0
    W=W+t1
  else:
    t=1
    W=W+t1
print(W)
# zadanie 10
# for i in range(1,1001):
#   if(i**2%10==i or i**2%100==i or i**2%1000==i):
#     print(i)
# 6
# 6a
