import calendar
import random
'''
year=2026
month=6
print(calendar.month(year,month))
'''
'''
year=2026
print(calendar.calendar(year))

while True:
    y=int(input("enter year"))
    m=int(input("enter month"))
    print(calendar.month(y,m))
'''
'''
#date and time
from datetime import date
a=date.today()
print(a)

from datetime import datetime
a=datetime.now()
print(a)
'''
'''
import time
a=time.time()
print(a)#apoch time like from 1970 counts all seconds
b=time.localtime(a)
print(b)
timesec=b.tm_sec
print(f'todays date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}')

print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
'''
'''
import time
for i in range(10):
    print(random.randint(1,100))
    time.sleep(2)
'''
import time
while True:
    pouch_a=time.time()
    b=time.localtime(pouch_a)
    print(f"{b.tm_hour}hours-{b.tm_min}minutes-{b.tm_sec}seconds")
    time.sleep(1)
