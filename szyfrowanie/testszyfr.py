# from hashlib import md5, sha1
# print(md5(b"test1").hexdigest())
# print(sha1(b"test1").hexdigest())
# passw="testtt"
# print(md5(passw.e).hexdigest())

napis = input()
szyfr = ""
for i in range(len(napis)):
    szyfr = szyfr + chr( 65 + (ord(napis[i]) - 65 + 3) % 26)
print(napis, szyfr)

