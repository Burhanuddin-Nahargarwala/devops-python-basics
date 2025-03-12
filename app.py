import time
import os

def log_event(event):
    """Logs an event with a timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("devops_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {event}\n")
    print(f"Logged event: {event}")

def check_disk_space():
    """Checks available disk space (simulated)."""
    # In a real-world scenario, you might use `shutil.disk_usage('/')`
    free_space = 50  # Simulating 50GB free space
    print(f"Available disk space: {free_space}GB")
    return free_space