import time

#############Time functions to return real dates and times also epoch#################### 

#time() number of seconds from epoch
print(time.time())

#gives information on time() functions
print(time.get_clock_info('time'))

#localtime() returns tuple with local time year date in GMT
print(time.localtime())

#gettime() returns tuple with local time year date in UTC  
print(time.gmtime())

#gmtime(0) returns tuple with year, date, and time of start of epoch
print(time.gmtime(0))

#naming time method to access tuple data
time_here = time.localtime()

#accessing year in tuple returned from localtime() using array 
print(f"year: {time_here[0]}")

#acsessing year in tupel returned from localtime() using name
print(f"year: {time_here.tm_year}")

#strftime() formats given function localtime, gmtime ect with placement fields '%Y %m' ect 
#see time python doc for list of placement fields
print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))

print("-" * 30)

########## More functions to measure elapsed time ###########################
#monotonic means clock dose not count backwards. perf_counter and monotonic functions both are monotonic

print(time.get_clock_info('monotonic'))
print(time.monotonic())

#perf_counter very precise timer good for timing code. better to uses this than monotonic
print(time.get_clock_info('perf_counter'))
print(time.perf_counter()) 

#times how long cpu takes to run a process rather than elapsed time
print(time.get_clock_info('process_time'))
print(time.process_time())

#see Python documentation on time