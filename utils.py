import csv

# Open file with append 'a' or write mode 'w'
def write_to_csv(filename, cpu_data, is_first_time):
    print("Writing to", cpu_data)
    if is_first_time:
        f = open(filename, 'w', newline="")
    else:
        f = open(filename, 'a', newline="")
    w = csv.DictWriter(f, cpu_data.keys())
    if is_first_time:
        w.writeheader()

    w.writerow(cpu_data)
    f.close()