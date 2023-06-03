import time
import datetime

lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(
        1
    )  # The sleep() function suspends (delays) execution of the current thread for the given number of seconds.

for i in lst:
    print(i)
