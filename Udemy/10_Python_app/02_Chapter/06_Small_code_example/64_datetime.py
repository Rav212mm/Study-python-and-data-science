from datetime import datetime

delta = datetime.now() - datetime(1900,12,31)

print(delta.days)
print(delta.seconds)

then = datetime(1200,3,1,12,22,2)
print(then)

now = datetime.now()
print(now)

whenever = datetime.strptime('2017-02-12-12-23', '%Y-%m-%d-%H-%M')
print(whenever)

print(whenever.strftime('%Y'))

print(whenever.strftime('%Y-%m-%d-%H-%M-%S'))

print(dir(datetime))
print(whenever.month, whenever.day, whenever.year)
