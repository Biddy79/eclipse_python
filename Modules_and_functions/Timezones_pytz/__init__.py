import pytz
import datetime
#pytz gets its time zone information form the data base iana: Internet Assigned Numbers Authority 

#store country in a variable
country = 'Canada/Mountain'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display) #setting tz object to tz_to_display

#print out country and its local time
print(f"The time in {country} is {local_time}")
#print out the utc time 
print(f"UTC is {datetime.datetime.utcnow()}")

print("-" * 30)

#list all time zones 
for x in pytz.all_timezones:
    print(x)
    
print("-" * 30)
    
#list a dictionary of country name. key is OS 01336 Country code e.g: GB, AU ect...
for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])
    
print("-" * 30)
#############################################    
#SOME COUNTRYS HAVE MORE THAN ONE TIME ZONE THEFORE YOU MAY WANT TO LIST ALL THE TIME ZONES FOR 
#A GIVEN COUNTRY. YOU ME BE TEMPTED TO DO SO LIKE THIS 

#THIS WILL GIVE ERROR AS BOTH pytz.country_names[x] AND pytz.country_timezones[x] DO NOT AVES THE 
#SAME KEYS AS THERE IS NO TIME ZONE FOR BV:BOUVET ISLAND. THERFOR WE CARNT USE THE SAME KEY
#FOR BOTH pytz.country_names[x] and pytz.country_timezones[x]

#for x in sorted(pytz.country_names):
#    print(f"{x}, {pytz.country_names[x]}, {pytz.country_timezones[x]} ")
    
#THE WAY TO DO THIS is by using .get(x) THIS WILL RETURN NONE IF pytz.country_timezones[x]
#IS NOT IN THE LIST AND WILL THERFOR NOT SHOW ERROR
################################################


for x in sorted(pytz.country_names):       #note the get(x)!!
    print(f"{x}, {pytz.country_names[x]}, {pytz.country_timezones.get(x)}")
    
print("-" * 30)
    
#list country time zone if there is one 
for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}", end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print(f"\t \t{zone}: {local_time}")
    else:
        print("\t \tNo time zone defined")



