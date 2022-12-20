# zadanie 1
# x = int(input())
# s=0
# for i in range(x):
#   a = int(input())
#   s=s+a
# print(s)
# zadanie 2
# q = int(input())
# t1 = 0
# for i in range(1,q+1):
#   if (q%i==0):
#     t1=t1+1
# if (t1==2):
#   print("tak")
# else:
#   print("nie")
# zadanie 3
# q = int(input())
# t1 = 0
# for i in range(1,q):
#   if (q%i==0):
#     t1=t1+i
# if (t1==q):
#   print("tak")
# else:
#   print("nie")
# ekseryment
# for q in range(1,10000000):
#   t1 = 0
#   for i in range(1,q):
#     if (q%i==0):
#       t1=t1+i
#   if (t1==q):
#     print(q)
# zadanie 4
# a, b=int(input()), int(input())
# while b>0:
#   a, b = b, a%b
# if a==1 :
#   print("tak")
# zadanie 5 wersja nauczyciela
# n = int(input())
# for i in range(10,20):
#   x=n
#   y=i
#   while y>0:
#     x,y=y,x%y
#   nwd=x
#   if(x==1):
#     print(f"TEst: {n}, {i}")
# zadanie 6 wersja nauczyciela
# a, b = int(input()), int(input())
# x = b
# y = a
# while x!=y:
#   if x>y: x-=y
#   if y>x: y-=x
# c = a//x
# d = b//x
# print(f"{a}/{b}={c}/{d}")
# test
# import random
# r = random.randint(0,10)
# print(r)
# zadanie 7
# a=int(input("*/b:"))
# b=int(input("a/*:"))
# c=b
# d=a
# c1=c
# d1=d
# while c!=d:
#   if c>d: c-=d
#   if d>c: d-=c
# e=c1//c
# f=d1//c
# print(f"{a}/{b} mieszana {c1}/{d1} = {e}/{f}")
# zadanie 8
# T=[]
# print("test")
# for i in range(2,10001):
#   suma1=0
#   suma2=0
#   for j in range(1,i):
#     if(i%j==0):
#       suma1+=j
#   T.append(suma1)
#   for k in range(1,suma1):
#     if(suma1%k==0):
#       suma2+=k
#   if(i==suma2 and suma1 != suma2 and suma2 not in T):
#     print(f"({suma1},{suma2})")
# zadanie 9
def czy_pierwsza(n):
  for i in range(2,n):
    if n%i==0:
      return False
  return True
for i in range(10,100):
  for j in range(2,i):
    if i%j==0:
      if czy_pierwsza(j) and czy_pierwsza(i//j):
        print(i,end=" ")
        break