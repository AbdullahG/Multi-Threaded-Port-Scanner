# Multi-Threaded-Port-Scanner
The script tries to connect to a server over TCP/IP with the port numbers(given as hardcoded) and it determines the ports are whether open or closed.
It is multi-threaded. So that, it decrease the scanning time. 
It had scaned 65535 ports in approximately 9 minutes with 5000 threads and ~200 mb memory usage.

Example Output:
Total Thread Number: 5000
Started in: Mon Mar 28 02:12:10 2016 End: Mon Mar 28 02:21:26 2016
open port number: 4
22,80,443,9411
