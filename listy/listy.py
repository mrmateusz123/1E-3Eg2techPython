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


#zadanie 5

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