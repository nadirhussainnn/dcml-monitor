import psutil

'''
This function reads CPU usage from the system and prints it.
return: None
'''
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f'CPU Usage: {cpu_percent}%')

'''
This function reads CPU times
return: A dictionary containing 'user_time', 'idle_time' and 'kernel_time'
'''
def read_cpu_times():
    cpu_times = psutil.cpu_times() # Returns a tuple of CPU times in user, kernel modes etc

    # print ("IDLE Time: {} , USER Time: {}".format(cpu_times.idle, cpu_times.user))
    # Because we want to export this data for ML, so we may want to write to CSV

    data={"user_time": cpu_times.user, "idle_time": cpu_times.idle}
    data["kernel_time"] = cpu_times.system # Another way of adding keys to dictionary
    return data
