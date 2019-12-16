import hashlib,time

def md5s(date):
    md = hashlib.md5(date.encode('utf-8'))
    return md.hexdigest()


date = '123456'
# s = hashlib.md5(date)
# print(type(s.hexdigest()))
# name = s.hexdigest()
# print(name)

# print(md5s(date))

print(time.ctime())










