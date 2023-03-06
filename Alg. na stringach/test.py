# s=input()
# for i in s:
#   print(chr(ord(i)+1))
# for i in range(len(s)):
#   print(ord(s[i]))

# L = [7,4,5,2]
# L.sort()
# print(s,L)

# L = list(s)
# R = L.copy()
# R.reverse()
# print(L)
# L.sort()
# print(L)
# w = "".join(L)
# print(w)
# if(R == L):
#   print("tak")
# else:
#   print("nie")

# for i in range(len(s)//2):
#   if(s[i]!=s[len(s)-1-i]):
#     exit("NIE")
# exit("TAK")
# # L[start:stop:step]
L = [i**2 for i in range(1,10)]
print(L)
print(L[:4])
print(L[::2])
print(L[1::2])
print(L[1:6:2])
print(L[6:1:-2])
print(L[len(L)-4::1])
print(L[:4:-1])