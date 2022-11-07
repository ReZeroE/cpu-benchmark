# cpu-benchmark
Lightweight tool for single and multi core CPU benchmarks. MIT Licensed.

```
Supported OS platforms:
 - Windows
 - macOS(Darwin)
 - Linux

Single-core CPU Benchmark by Alex Dedyura
Multi-core CPU Benchmark by Kevin Liu
```

## How to run
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
