# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# print(chr(65))
# print(chr(75))
# print(chr(89))

# for i in range(0,1000):
#  print(chr(i),end=" ")
#  print(i)

# print(chr(ord("C")))
# print(chr(ord("C")+1))
  
# napis = input()
# szyfr=""
# for i in range(len(napis)):
#   szyfr = szyfr + chr(65+(ord(napis[i])-65+3)%26)
# print(napis,szyfr)
a, b ,c ,d = int(input("a/*:")), int(input("*/b:")), int(input("c/*:")), int(input("*/d:"))
w=b*d
t=b
t1=d
while d>0:
  b, d = d, b%d
w=w//b
b=t
d=t1
t=w//t*a
t1=w//t1*c
t2=t1+t
print(f"{a}/{b}+{c}/{d}={t2}/{w}")