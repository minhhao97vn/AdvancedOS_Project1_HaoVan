# AdvancedOS_Project1_HaoVan

<h2><b>Overview</b></h2>
<ul>
  <li>The purpose of this project is retrieving, comparing and presenting process profiling data.</li>
  <li>Algorithms for comparison: Fibonacci search and Jump search.</li>
</ul>

<h2><b>Guidelines</b><br></h2>
 There are 5 python file in the project: 
<ul>
  <li><b>fibonacci_search.py</b>: run and get process information of Fibonacci search algorithm.</li>
  <li><b>jump_search.py</b>: run and get process information of Jump search algorithm.</li>
  <li><b>fibonacci_jump_concurrent.py</b>: run and get process information of Fibonacci search and Jump search algorithm concurrently.</li>
  <li><b>generating_data.py</b>: generate input data before running algorithms. </li>
  <li><b>visualization.py</b>: visualize the information from system. </li>
</ul>
Steps to run the source code:
<ul>
  <li>The source code is implemented with Python 3 and uses packages: math, json, matplotlib, time, psutil, os, bisect, multiprocessing.</li>
  <li>Open the terminal or command line and change dir to the folder which contains this project.</li>
  <li>Run <b>generating_data.py</b> to generate input data and write to input.json file.</li>
  <li>Run <b>fibonacci_search.py</b>, information will be printed on the terminal and a .json file.</li>
  <li>Run <b>jump_search.py</b>, information will be printed on the terminal and a .json file.</li>
  <li>Run <b>fibonacci_jump_concurrent.py</b>, information will be printed on the terminal and a .json file.</li>
  <li>Run <b>visualization.py</b>, charts will be showed so as to help user analyze the information.</li>
</ul>

<h2><b>Experiment</b></h2>
This experiments:
<ul>
  <li>Data: Array contains 49,995,386 integers which have values from 0 to 100,000,000 and target number is 81,905,004. File <b>input.json</b>.</li>
  <li>Hardware: Macbook Pro 2019, macOS Catalina, processor: 2.3GHz 8-Core Intel Core I9, RAM: 16GB.</li>
</ul>
<h2><b>Analysis of results</b></h2>
The running time and system profiling were recorded and there are two types of information: for running algorithm only and running program. <br>

![run_time_algo](https://i.imgur.com/DMSW02R.png) ![run_time_program](https://i.imgur.com/mOnWprA.png) 

From the charts "Running time for algorithm only", we can observe that both two searching algorithms have good running time (<= 0.014 second) with large number of elements in array (~50 millions) but Fibonacci search algorithm has better running time in both running alone and running concurrently condition. This is make sense because Fibonacci search has O(log(n)) complexity and Jump search has O(sqrt(n)).

The running time of whole programs (including time for loading data, package, executing algorithm, ...) are similar when running alone and Fibonacci search is higher when running concurrently. When running concurrently, the Fibonacci search maybe the program which load the data first, so the difference maybe come from IO time. <br>

![cpu_perc](https://i.imgur.com/6enNfzl.png)  

Both algorithms had high usages of CPU when running on both alone and concurrently mode. <br>

![rss_vms_algo](https://i.imgur.com/EPoawdt.png) ![rss_vms_program](https://i.imgur.com/D8hnQPj.png) 

The RSSs and VMSs for running algorithm only are really small in chart "RSS and VMS for running algorithm". In the concurrent mode, the VMS of jump_concurrent is near to 0. 
<br>
![pf_pi_algo](https://i.imgur.com/Lcdb4Hf.png) ![pf_pi_program](https://i.imgur.com/gBXYVvx.png)

In the chart "Pagefaults and pageins for running algorithm", we can easily observe that Jump search algorithm had high number of page fault when running in both alone and concurrent mode and this number is much higher than the number from Fibonacci search. The number of page faults in concurrent mode is not much different from the number in alone mode.

We can also see that the number of page fault of whole program is very high when comparing the above charts. 

The number of page in is very small (all are zeoros except only 14 for fibonacci_concurrent and 14 for jump_concurrent).
