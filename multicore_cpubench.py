#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Copyright (c) 2021-2022 Kevin Liu <kevinliu@vt.edu>
# CPU Benchmark Tool (single & multi core) 
# MIT License
# Hosted at: https://github.com/ReZeroE/cpu-benchmark
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import time
import argparse
import cpuinfo 
import platform
from multiprocessing import Process, Manager, cpu_count
from singlecore_cpubench import run_single_core_bench

PROCESSES = cpu_count() - 1
BENCHMARK_LOAD = 50000 # can be 1000, 5000, 10000...

verbose = False
start_time = time.time()

def metadata():
    os_version  = platform.system()
    cpu_brand   = cpuinfo.get_cpu_info()['brand_raw']
    cpu_arch    = cpuinfo.get_cpu_info()['arch_string_raw']
    os_ver      = str(os_version) + " " + platform.release()
    print('Single-core CPU Benchmark by Alex Dedyura\nMulti-core CPU Benchmark by Kevin Liu\nSupports Windows, macOS(Darwin), and Linux')
    print('CPU: ' + cpu_brand)
    print('Logical Cores:', cpu_count())
    print('Arch: ' + cpu_arch)
    print('OS: ' + os_ver)
    print("")


def run_multiprocess_benchmark():
    jobs = []
    manager = Manager()
    return_dict = manager.dict()

    for i in range(PROCESSES):
        proc = Process(target=run_single_core_bench, args=(i, BENCHMARK_LOAD/PROCESSES, return_dict))
        jobs.append(proc)
        proc.start()
        if verbose: print(f"[Process {i}] has started...")
    if not verbose: print("Benchmark in progress...")

    for j_proc in jobs: 
        j_proc.join()
    
    vals = return_dict.values()
    vals.sort(key=lambda x: x[0])

    avg_time = 0
    print("\nBenchmark Completed:")
    for process_ret in vals:
        if verbose: print(f"[Process {process_ret[0]}] {process_ret[1]} seconds")
        avg_time += process_ret[1]

    print(f"Avg. Process Time: {round(avg_time / PROCESSES, 3)} seconds")
    print(f"Program Execution Time: {round(time.time() - start_time, 3)} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-v', '--verbose', dest="verbose", default=False, action="store_true", help='Verbose output')
    parser.add_argument('-p', '--processes', type=int, dest="processes", default=None, help='Number of forked processes for multiprocessing benchmark (Default to the number of installed logical cores - 1)')
    parser.add_argument('-l', '--load', type=int, dest="load", default=None, help='Benchmark load value, default to 50000 (Suggested: 5000~100000)')


    args = parser.parse_args()
    if args.processes != None:
        PROCESSES = args.processes
    if args.load != None:
        BENCHMARK_LOAD = args.load
    verbose = args.verbose

    metadata()
    run_multiprocess_benchmark()