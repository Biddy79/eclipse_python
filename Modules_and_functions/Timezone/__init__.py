import time

print(f"The epoch on this system starts at {time.strftime('%c', time.gmtime(0))}")

print(f"The curent timezone is {time.tzname[0]} with an offset of {time.timezone}")

if time.daylight != 0:
    print("\t Daylight saving time is in effect for this locations")
    print(f"\t The DTS timezone is {time.tzname[1]}")
    
print(f"Local time is {time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())}")

print(f"UTC time is {time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())}")

print("-" * 30)

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())