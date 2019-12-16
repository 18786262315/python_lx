import hashlib




date = '123456'.encode('utf-8')
s = hashlib.md5(date)
print(type(s.hexdigest()))
name = s.hexdigest()
print(name)