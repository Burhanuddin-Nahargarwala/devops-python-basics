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


# Simple caching function to store and reuse computed results

cache = {}  # Dictionary to store computed results

def get_square(n):
    if n in cache:
        print(f"Fetching from cache: {n}^2 = {cache[n]}")
        return cache[n]
    
    print(f"Computing and storing: {n}^2")
    result = n ** 2
    cache[n] = result
    return result

if __name__ == "__main__":
    log_event("Script started.")
    check_disk_space()
    log_event("Checked disk space.")

    # Example Usage
    print(get_square(5))  # Computes and stores 5^2
    print(get_square(5))  # Fetches from cache
    print(get_square(3))  # Computes and stores 3^2