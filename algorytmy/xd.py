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
t = 0
a = int(input())
for i in range(1,a+1):
  if (a%i==0):
    t+=1
if(t==2):
 print("tak")
else:
  print("nie")