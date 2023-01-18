from hashlib import md5, sha1
print(md5(b"test1").hexdigest())
print(sha1(b"test1").hexdigest())
passw="testtt"
print(md5(passw.e).hexdigest())