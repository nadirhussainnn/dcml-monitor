from utils import write_to_csv
from time import sleep
from cpu_probe import read_cpu_times
from memory_probe import read_memory_usage
    
if __name__ == '__main__':
    
    # We access different probes of a system to monitor it. For example: Memory, CPU, Network etc
    # Probe can be seen as socket, or interface

    is_first_time = True
    while True:
        cpu_data= read_cpu_times()
        memory_data= read_memory_usage()
        write_to_csv('cpu_usage.csv', cpu_data | memory_data, is_first_time)  # Write to CSV every second.  You can adjust this interval as needed. 1 second is a common interval.
        is_first_time = False  # Only write header row once.  After that, write to CSV every second.  This prevents appending to the CSV file with each iteration.

        sleep(1)