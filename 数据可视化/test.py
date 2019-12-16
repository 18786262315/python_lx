from faker import Faker

f=Faker(locale='zh_CN')

print(f.date(pattern="%Y-%m-%d %H:%M:%S", end_datetime=None))

print(f.pyint(2))

nn = [ f.pystr() for i in range(10)  ]

print(nn)
