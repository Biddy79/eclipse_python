import time
import random



input("press enter to start")

wait_time = random.randint(1, 7)

time.sleep(wait_time)

start_time = time.perf_counter()

input("Press enter to stop")

end_time = time.perf_counter()

print("Time at start of program " + time.strftime("%X", time.localtime(start_time)))

print("Time at end of program " + time.strftime("%X", time.localtime(end_time)))

print(f"your reaction time in seconds:  {end_time - start_time}")







