import hashlib

def md5s(date):
    md = hashlib.md5(date.encode('utf-8'))
    return md.hexdigest()


date = '64cb26c2c87c4'
# s = hashlib.md5(date)
# print(type(s.hexdigest()))
# name = s.hexdigest()
# print(name)

print(md5s(date))











