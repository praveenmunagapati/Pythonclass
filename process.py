"""
1️⃣ What is Multiprocessing?
    Theory

    Multiprocessing means running multiple processes simultaneously
    using multiple CPU cores.
    A process is an independent program with its own memory space.
    Unlike threads, processes do not share memory.
    Python provides multiprocessing support using the multiprocessing.

    Multiprocessing is useful for CPU-bound tasks such as:
    image processing
    scientific computations
    machine learning calculations
    data analysis

2️⃣ Process vs Thread
    Theory
    Feature	        Process	            Thread
    Memory	        Separate	        Shared
    Speed	        Slower to create	Faster
    Communication	Harder	            Easier
    Best for	    CPU tasks	        I/O tasks

    Threads in Python are created using the threading.

3️⃣ Creating a Process
    Theory
    A process can be created using the Process class.
    Steps

    1️⃣ Import multiprocessing
    2️⃣ Create process object
    3️⃣ Start the process

    Example
    """
import multiprocessing

def task():
    print("Process running")

p = multiprocessing.Process(target=task)

p.start()
p.join()
# Output
# Process running

# 4️⃣ Multiple Processes Example
# Program
import multiprocessing
def task(name):
    print("Running process:", name)

p1 = multiprocessing.Process(target=task, args=("Process1",))
p2 = multiprocessing.Process(target=task, args=("Process2",))

p1.start()
p2.start()
p1.join()
p2.join()
# Possible Output
# Running process: Process1
# Running process: Process2
#Order may vary because processes run concurrently.

# 5️⃣ Example: CPU Intensive Task
# Program

import multiprocessing
def square(num):
    print(num * num)

numbers = [1,2,3,4]
processes = []
for n in numbers:
    p = multiprocessing.Process(target=square, args=(n,))
    processes.append(p)
    p.start()
for p in processes:
    p.join()
# Output
# 1
# 4
# 9
# 16
# 6️⃣ Getting Process ID
# Theory
# Each process has a unique process ID (PID).
# We can obtain it using the os module.
# Example
import multiprocessing
import os
def show_pid():
    print("Process ID:", os.getpid())
p = multiprocessing.Process(target=show_pid)
p.start()
p.join()

# Output Example
# Process ID: 5432
# 7️⃣ Sharing Data Between Processes
# Theory
# Since processes do not share memory, special mechanisms are required.
# Python provides:
# Queue
# Pipe
# Shared memory
# Example Using Queue

import multiprocessing

def worker(q):
    q.put("Hello from process")
q = multiprocessing.Queue()
p = multiprocessing.Process(target=worker, args=(q,))
p.start()
p.join()
print(q.get())

# Output
# Hello from process
# 8️⃣ Process Pool
# Theory
# A process pool allows us to reuse a group of processes.
# Useful when performing the same task on many inputs.
# Python provides Pool class.
# Example

import multiprocessing
def square(n):
    return n*n
if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        result = pool.map(square, [1,2,3,4,5])
    print(result)

# Output
# [1, 4, 9, 16, 25]

# 9️⃣ Why Multiprocessing is Important
# Theory
# Python has a limitation called Global Interpreter Lock (GIL).
# The GIL allows only one thread to execute Python bytecode at a time.
# Multiprocessing bypasses this limitation because each process has its own interpreter.

# 🔟 Real World Applications
# Multiprocessing is widely used in:
# Machine learning pipelines
# Scientific simulations
# Video processing
# Large-scale data processing
# Libraries like NumPy and Pandas often benefit from multiprocessing for heavy computations.

# 1️⃣1️⃣ Multiprocessing Flow
# Main Program
#      │
#      ├── Process 1
#      │      └─ Task
#      │
#      ├── Process 2
#      │      └─ Task
#      │
#      └── Process 3
#             └─ Task

# Each process runs independently on CPU cores.
#
# 🧠 Summary
# Concurrency in Python
#         │
#         ├── Threads
#         │     └─ I/O tasks
#         │
#         ├── Async / Await
#         │     └─ Network tasks
#         │
#         └── Multiprocessing
#               └─ CPU tasks

# 🎯 Key Points for Students
# ✔ Multiprocessing uses multiple CPU cores
# ✔ Each process has separate memory
# ✔ Implemented using multiprocessing module
# ✔ Best for CPU-bound tasks
# ✔ Avoids Python GIL limitation

