import time
import datetime
import pytz

#from datetime module you can pass in your own date and time as parameter to datetime()
print(datetime.datetime(1979,8,12,12,35,0))

country = 'Canada/Mountain'
#pytz object is returned by pytz.timezone() country is added as a parameter 
print(type(pytz.timezone(country)))

#datetime.now() takes a pytz object 
print(datetime.datetime.now(pytz.timezone(country)))

#a better way to write this is by assigning pytz.timezone() to a variable 
tz_to_display = pytz.timezone(country)
#We now set tz object = to tz_to_display in the parameter  
local_time = datetime.datetime.now(tz = tz_to_display)
#we can then print out the country and time
print(f"The time in {country} is {local_time}")

#from pytz module all.timezones returns a list. entries in a list can be accessed using array syntax
print(pytz.all_timezones[3])

#or we can see all entries using for loop 
for x in pytz.all_timezones:
    print(x)

print("-" * 30)
#from pytz module .country_names return a dictionary key is string OS 01336 Country code e.g: GB, AU ect..
print(pytz.country_names['GB'])

