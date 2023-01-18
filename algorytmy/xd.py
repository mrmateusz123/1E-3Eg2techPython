# import random
# t = []
# a = int(input())
# for i in range(a):
#   r = random.randint(0, 10)
#   t.append(r)
#   print(t[i], i+1)
# a = int(input())
# t=0
# for i in range(1,a):
#   if(a%i==0):
#     t+=i
# if a==t:
#   print("tak")
# else:
#   print("nie")

# t = 0
# a = int(input())
# for i in range(a):
#   t1 = int(input())
#   t+=t1
# print(t)
# t = 0
# a = int(input())
# for i in range(1,a+1):
#   if (a%i==0):
#     t+=1
# if(t==2):
#  print("tak")
# else:
#   print("nie")
# a = int(input())
# b = int(input())
# c = int(input())
# if(a>b>c):
#   print("malejący: TAK")
# else:
#   print("malejący: NIE")
# if(a<b<c):
#   print("rosnący: TAK")
# else:
#   print("rosnący: NIE")
# if(a-b==b-c or c-b==b-a):
#   print("arytmetyczny: TAK")
# else:
#   print("arytmetyczny: NIE")
# if(a/b==b/c or c/b==b/a):
#   print("geometryczny: TAK")
# else:
#   print("geometryczny: NIE")

# for i in range(100,1000):
#   if(i%8==0 and i%16!=0):
#     print(i)

# t1=0
# t2=0
# for i in range(10,100):
#   if(i>0 and i%7==0):
#     t1=i
# for i in range(100,1000):
#   if(i%t1==0):
#     t2+=1
# print(t2)

# a=int(input())
# print(a%10)
# print(a//10%10)
# print(a//100%10)
# print(a//1000%10)
# print(a//10000%10)