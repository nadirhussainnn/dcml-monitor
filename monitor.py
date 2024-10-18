from time import sleep
import psutil

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f'CPU Usage: {cpu_percent}%')

def read_cpu_times():
    cpu_times = psutil.cpu_times()
    print ("IDLE Time: {} , USER Time: {}".format(cpu_times.idle, cpu_times.user))

if __name__ == '__main__':
    while True:
        get_cpu_usage()
        read_cpu_times()
        sleep(1)