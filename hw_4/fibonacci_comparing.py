import multiprocessing
import threading
import time

def fibonacci_numbers(n):
    if n < 2:
        return n
    
    return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)

def run_sync(n, num_runs = 10):
    start_time = time.time()
    
    for _ in range(num_runs):
        fibonacci_numbers(n)

    return time.time() - start_time

def run_threads(n, num_runs = 10):
    start_time = time.time()
    
    threads = []
    for _ in range(num_runs):
        thread = threading.Thread(target = fibonacci_numbers, args = (n, ))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    return time.time() - start_time

def run_processes(n, num_runs = 10):
    start_time = time.time()
    
    processes = []
    for _ in range(num_runs):
        process = multiprocessing.Process(target = fibonacci_numbers, args = (n, ))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()
        
    return time.time() - start_time

n = 32

with open("artifacts/fibonacci_time.txt", "w") as file:
    file.write(f"Synchronous, n = {n}: {run_sync(n)}\n")
    file.write(f"Threading, n = {n}: {run_threads(n)}\n")
    file.write(f"Multiprocessing, n = {n}: {run_processes(n)}")
