from time import sleep, perf_counter as pc
t0 = pc()
sleep(1)
print(pc()-t0)
