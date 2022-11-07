#!/usr/bin/python3
#Python CPU Benchmark by Alex Dedyura (Windows, macOS, Linux)

import time
import platform
import cpuinfo 

os_version = platform.system()

def run_single_core_bench(thread_id, load, return_dict=None):
  start_benchmark = load # change this if you like (sample: 1000, 5000, etc)
  start_benchmark = int(start_benchmark)

  repeat_benchmark = 1 # attemps, change this if you like (sample: 3, 5, etc)
  repeat_benchmark = int(repeat_benchmark)

  average_benchmark = 0

  for _ in range(0, repeat_benchmark):

    start = time.time()

    for _ in range(0, start_benchmark):
      for x in range(1,1000):
        3.141592 * 2**x
      for x in range(1,10000):
        float(x) / 3.141592
      for x in range(1,10000):
        float(3.141592) / x

    end = time.time()
    duration = (end - start)
    duration = round(duration, 3)
    average_benchmark += duration
    # print('Time: ' + str(duration) + 's')

  average_benchmark = round(average_benchmark / repeat_benchmark, 3)
  # print('Average: ' + str(average_benchmark) + 's')

  if return_dict == None:
    pass
  else:
    return_dict[thread_id] = thread_id, average_benchmark

  return thread_id, average_benchmark

if __name__ == "__main__":
  print(run_single_core_bench(-1, 50000))