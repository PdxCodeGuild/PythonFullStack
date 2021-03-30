




import time
from datetime import datetime, timedelta

print(time.time()) # the number of seconds since midnight jan 1st 1970


d = datetime.now()

# print(f'{d.month}/{d.day}/{d.year}')

print(d.strftime('%m/%d/%Y'))
d += timedelta(days=1)
print(d.strftime('%m/%d/%Y'))



