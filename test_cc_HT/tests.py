import hashlib




date = '64cb26c2c87c4920917c766901ba7b4d'.encode('utf-8')
s = hashlib.md5(date)
print(type(s.hexdigest()))
name = s.hexdigest()
print(name)