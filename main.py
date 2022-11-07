#!/usr/bin/env python
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

import os
import time
import psutil
import cpuinfo 
import platform

BAR_LEN = 50

os_version = platform.system()
cpu_brand   = cpuinfo.get_cpu_info()['brand_raw']
cpu_arch    = cpuinfo.get_cpu_info()['arch_string_raw']
os_ver      = str(os_version)

print('Python CPU Benchmark by Alex Dedyura (Windows, macOS(Darwin), Linux)\nMultitheading Benchmark by Kevin Liu')
print("String benchmark in 3 seconds..."); time.sleep(3)


benchmark_started = False
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    str_base = ['=']
    str_emp  = [' ']
    cpu_usage_str = []
    cpu_usages = psutil.cpu_percent(interval=0, percpu=True)
    for i, cpu in enumerate(cpu_usages):
        l = int(cpu / 100 * BAR_LEN)

        bar = "".join(str_base * l)
        emp = "".join(str_emp * (BAR_LEN - l))
        str_rep = f"CPU {i}:\t[{bar}{emp}] -> {cpu}"
        cpu_usage_str.append(str_rep)


    print('CPU: ' + cpu_brand)
    print('Arch: ' + cpu_arch)
    print('OS: ' + os_ver)
    print("\n".join(cpu_usage_str))
    time.sleep(3)