import sys
import datetime

Dates=datetime.date.today()
now=datetime.datetime.now()

print(Dates)
print(now.strftime('%Y-%m-%d %H:%M:%S'))


print('Python version')
print(sys.version)
print('Python sys_version')
print(sys.version_info)
print("\tA","B\n","C")