# cpu-benchmark
Lightweight tool for single and multi core CPU benchmarks. MIT Licensed.

<img src="https://i.imgur.com/cZWLCEL.png" width="400" height="auto" align="left"/>
<ul>
  
```
Supported OS platforms:
 - Windows
 - macOS(Darwin)
 - Linux

Multi-core CPU Benchmark by Kevin Liu
Single-core CPU Benchmark by Alex Dedyura
```

| [How to run](https://github.com/ReZeroE/cpu-benchmark#how-to-run) |  -  |
[Benchmark reference](https://github.com/ReZeroE/cpu-benchmark#benchmark-reference) |

</ul>
<br clear="left"/>

***

# How to run
### 1. Installation
```
git clone https://github.com/ReZeroE/cpu-benchmark.git
```

### 2. Run Benchmark

  - Multicore Benchmark
    - `-h | --help` Display help message
    - `-v | --verbose` Verbose Output
    - `-p | --processes` The number of cores to run the benchmark on (Default to the number of installed logical cores - 1)
    - `-l | --load` Benchmark load value, default to 50000 (Suggested: 5000~100000)
 ```
 python ./multicore_cpubench
 python ./multicore_cpubench -v --processes 16 --load 60000
 ```
  - Singlecore Benchmark
 ```
 python ./singlecore_cpubench
 ```

# Benchmark Reference
Reference Command:
 ```
$ python ./multicore_cpubench -l 50000
 ```
|  | CPU  | Logical Cores | OS | Avg. Process Time | Run Time
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| :heavy_check_mark: | Intel(R) Xeon(R) Gold 5218 | 64 | CentOS | 5.674 seconds | 6.288 seconds |
| :heavy_check_mark: | Apple M2 | 8 | Darwin | 24.721 seconds | 27.168 seconds |
| :heavy_check_mark: | i9-12900K | 24 | x86_64 | 3.215 seconds | 5.656 seconds |
| :heavy_check_mark: | i9-9900K | 16 | x86_64 | 8.825 seconds | 11.935 seconds |
| :heavy_check_mark: | AMD Ryzen 7 4800H | 9 | Windows 11 | 12.572 seconds | 16.202 seconds |
| :o: | i9-11900H | 16 | Windows 11  | untested | untested |
| :o: | i5-9300H | 8 | Windows 11  | untested | untested |
| :o: | i9-11900H | 16 | Windows 11  | untested | untested |



