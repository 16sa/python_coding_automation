# shutil module: A Python library for high-level file operations, including checking disk usage.
# psutil module : A powerful cross-platform library for retrieving information on running processes 
#  and system utilization.
#!/usr/bin/env python3
import shutil
import random

CPU_THRESHOLD = 80.0
MEM_THRESHOLD = 85.0
DISK_THRESHOLD = 90.0

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    return (used / total) * 100

def check_cpu_usage():
    # In a real script, you would use psutil.cpu_percent()
    return random.uniform(10.0, 95.0)

def check_memory_usage():
    # In a real script, you would use psutil.virtual_memory().percent
    return random.uniform(20.0, 98.0)

def main():
    print("--- Running System Health Check ---")
    
    cpu = check_cpu_usage()
    mem = check_memory_usage()
    disk = check_disk_usage()

    print(f"CPU: {cpu:.2f}% | Memory: {mem:.2f}% | Disk: {disk:.2f}%")

    if cpu > CPU_THRESHOLD:
        print(f"ALERT: High CPU usage detected: {cpu:.2f}%")
    
    if mem > MEM_THRESHOLD:
        print(f"ALERT: High Memory usage detected: {mem:.2f}%")

    if disk > DISK_THRESHOLD:
        print(f"ALERT: Low Disk space detected: {disk:.2f}% used")

    print("--- Check Complete ---")

if __name__ == "__main__":
    main()