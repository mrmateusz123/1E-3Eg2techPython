# a=int(input())
# b=int(input())
# while (a!=b):
#   if(a>b):
#     a=a-b
#   else:
#     b=b-a
# print(a)
# a, b=int(input()), int(input())
# while a!=b:
#   if a>b: a=a-b
#   else: b=b-a
# print(a)
# a, b=int(input()), int(input())
# while b>0:
#   a, b = b, a%b
# print(a)
# print("1 sposób")
a, b=int(input()), int(input())
w=a*b
while b>0:
  a, b = b, a%b
# print("NWD",a)
# print("NWW",w//a)