# from math import gcd # NWD
# print(gcd(12,16))

# 1.Wybór 2 dużych liczb pierwszych
p = 101
q = 103
print(p,q)
# 2.stworzenie funkcji F = (p-1 * q-1) i znalezienie n = p*q
F = (p-1) * (q-1)
n = p * q
print(n)
print(F)
# 3. znalezienie klucza publicznego e: NWD(F,e) = 1
from math import gcd
for i in range(2,F):
  if(gcd(i,F)==1):
    e=i
    break
print(e,n)
# 4.wygerenowanie klucza prywatnego d: d*e mod F = 1
for i in range(2,n):
  if((i*e)%F==1):
    d=i
    break
print(d,n)
# Przykład działania:
# c = x**e mod n (na szyrfogram)
# t = c**d mod n (na tekst jawny)
msg = input()
szyfrogram = ""
for i in msg:
  szyfrogram += chr((ord(i) ** e) % n)
print(szyfrogram)

jawny=""
for j in szyfrogram:
  jawny += chr((ord(j) ** d) % n)
print(jawny)
print(chr(100000))

