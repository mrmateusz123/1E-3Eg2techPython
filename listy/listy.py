# x = list(range(5))
# for item in x:
#   print(item)
# print(len(x), "ilość")
# print()
# for i in range(len(x)):
#   print(x[i])
# b = int(input("ile"))
# a = list(range(b))
# for i in range(len(a)):
#   c = int(input("liczba"))
#   a[i]=c
# for i in range(len(a)):
#   print(a[i])
# L=[3, 5, 8, 13, 17, 27]
# for elem in L:
#   print(elem,end=" ")
# print("\n")
# for i in range(len(L)):
#   print(L[i],end=" ")
# K = [4,7,5,7,3,3,2,8,7]
# print(K)
# K.append(3)
# print(K)
# print(K.count(7), "liczba ile 7")
# print(K.index(7), "gdzie pierwsza 7")
# K.insert(2,9)
# K.append(9)
# print(K)
# K.pop()
# print(K)
# K.reverse()
# print(K)
# K.sort() # sort(reverse=True)
# print(K)

# for i in range(K.count(7)):
#   K.remove(7)
# print(K)

# for i in range(K.count(7)):
#  K.pop(K.index(7))
# # print(K)

# print(max(K))

# K.sort(reverse=True)
# print(K[0])

# m = K[0]
# for i in K:
#   if i > m:
#     m = i
# print(m)


from random import randint
T = [randint(0, 100) for i in range(40)]
print(T)

#zadanie 1
# print(max(T))

#zadanie 2
# print(min(T))

#zadanie 3
# print(min(T), "-" ,max(T))

#zadanie 4
# S = list(set(T))
# print(S[len(S)-2])

#zadanie 5
# S = list(set(T))
# print(S[len(S)-(len(S)-1)])

#zadanie 6
# print(T.count(max(T)))

#zadanie 7
# print(T.count(min(T)))

#zadanie 8
# a = int(input())
# print(T.count(a))

#zadanie 9
# s=0
# for i in range(40):
#   s=s+T[i]
# print(round(s/len(T),1))

#zadanie 10
# s=0
# for i in range(0,40,2):
#   s=s+T[i]
# print(s)

#zadanie 11
# s=0
# for i in range(1,40,2):
#   s=s+T[i]
# print(round(s/len(T/2),1))

#zadanie 12
# l=len(T)
# l1=0
# for i in range(len(T)):
#   for j in range(len(T)):
#     if(T[i]==T[j]):
#       l1+=1
#     if(l1>1):
#       break
#   if(l1>1):
#     l=l-1
#   l1=0
# print(l)

#zadanie 13
# l=0
# for j in range(10,100):
#   for i in range(len(T)):
#     if(j==T[i]):
#       break
#     else:
#       l+=1
#     if(l==40):
#       print(j)
#   l=0

#zadanie 14
# l=len(T)
# l1=0
# for i in range(len(T)):
#   for j in range(len(T)):
#     if(T[i]==T[j]):
#       l1+=1
#     if(l1>1):
#       break
#   if(l1>1):
#     l=l-1
#   l1=0
# print(len(T)-l)

#zadanie 15
d1=0
d2=0
d3=0
s1=0
s2=0
s3=0
for i in range(len(T)):
  if(T[i]<=T[i+1] and d1==0):
    d1=i
  elif(T[i]>=T[i+1]):
    d2=i
    d3=d2-d1
    if(d3>s3):
      s1=d1
      s2=d2
      s3=d3
      d1=0
      d2=0
      d3=0
print(f"przedziały{s1}-{s2}")