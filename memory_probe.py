import psutil

"""
This function reads VM data from the system and uses it to update a dict
return: A dictionary containing the mem_total, mem_available - Free memory, and mem_percent
"""
def read_memory_usage():
    vm_data = psutil.virtual_memory()
    data_dict = {}
    data_dict["mem_total"] = vm_data.total
    data_dict["mem_available"] = vm_data.available
    data_dict["mem_percent"] = vm_data.percent
    print("Read memory usage", data_dict)
    return data_dict