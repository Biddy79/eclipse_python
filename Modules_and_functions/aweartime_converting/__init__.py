import datetime
import pytz

#When working with dates and time it is best to take the local time and convert to UTC time.  
#After completing all function with UTC then convert back to local time

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive loacl time {local_time}")
print(f"Naive UTC {utc_time}")

print("-" * 30)
#pytz.utc will be aware of offset in time zones. Note out put of below function +00:00 or +01:00
#This did not occur in the above functions out put above using datetime.datetime

#astimezone() will convert utc_time to time zone if no pytz.info is passed as parameter 
#this will default to local time zone 
awear_local_time = pytz.utc.localize(utc_time).astimezone()
awear_utc_time = pytz.utc.localize(utc_time)

print(f"Aware local time {awear_local_time} time zone {awear_local_time.tzinfo}")
print(f"Aware UTC time {awear_utc_time} time zone {awear_utc_time.tzinfo}")

print("-" * 30)


gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp()) # timesttamp() = seconds from beginning of epoch date of gap_time

s = 1445733000 # epoch 25/10/2015 at 1:30
t = s + (60 * 60) # 60 seconds in 1 min, 60 mins in 1 hour * 1445733000

gb = pytz.timezone('GB')

#creating a pytz info object using utc.loclize() and astimezone(gb).
#Note we are  working in UTC using utcfromtimestamp() 
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

#Here we have the same date due to British daylight saving where clock go back 1 hour at 2am 
#Take note that although we are working in UTC it is aware of time zone due to astimezone(gb) function.
#Therefore when outputting dt1 and dt2 we see +01:00 and +00:00 representing daylight savings

print(f"Seconds since epoch {t} {dt1}")
print(f"Seconds since epoch {t} {dt2}")
