import time

#time() number of secons from epoch
print(time.time())

#localtime() returns tuple with local time year date in GMT
print(time.localtime())

#gettime() returns tuple with local time year date in UTC  
print(time.gmtime())

#gettime(0) returns tuple with year date time of tart of epoch
print(time.gmtime(0))

#naming time method to acsess tuple data
time_here = time.localtime()

#acsessing year in tupel returned from localtime() using array 
print(f"year: {time_here[0]}")

#acsessing year in tupel returned from localtime() using name
print(f"year: {time_here.tm_year}")
