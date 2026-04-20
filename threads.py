"""
    1️ What is a Thread?

    Theory
    A thread is the smallest unit of execution inside a process.
    A program normally runs one task at a time:
    Task1 → Task2 → Task3
    But with threads, multiple tasks can run concurrently:
    Task1
    Task2
    Task3

    Threads are useful when a program needs to handle:
    multiple users
    background tasks
    downloading files
    network operations

    2️⃣ Multithreading in Python
    Theory
    Multithreading allows a program to execute multiple threads simultaneously.
    Python provides threading support using the **threading module.
    Threads are useful for I/O-bound tasks such as:
    web requests
    database queries
    file operations

    3️ Creating a Thread
    Theory
    To create a thread:
    Import the threading module
    Create a thread object
    Start the thread
    Example
"""

import threading
def display():
    print("Thread is running")
t = threading.Thread(target=display)
t.start()

# Output
# Thread is running

# 4️ Multiple Threads Example
# Program
import threading
def task1():
    print("Task 1 running")
def task2():
    print("Task 2 running")
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
# Output
# Task 1 running
# Task 2 running
#Order may vary because threads run concurrently.

# 5️ Using join() Method
# Theory
# The join() method makes the main thread wait until a thread finishes execution.
# Example
import threading
def work():
    print("Thread started")

t = threading.Thread(target=work)
t.start()
t.join()
print("Main thread finished")

# Output
# Thread started
# Main thread finished

# 6️ Thread with Arguments
# Example
import threading

def greet(name):
    print("Hello", name)
t = threading.Thread(target=greet, args=("Ravi",))
t.start()
# Output
# Hello Ravi

# 7️ Thread Using a Class
# Theory
# Threads can also be created by extending the Thread class.
# Example

import threading

class MyThread(threading.Thread):
    def run(self):
        print("Thread running")
t = MyThread()
t.start()

#8️ Example: Multiple Numbers Printing

import threading
def print_numbers():
    for i in range(5):
        print(i)
t = threading.Thread(target=print_numbers)
t.start()

# 9️ Thread Name
# Theory
# Each thread has a name.
# Example

import threading
def show():
    print(threading.current_thread().name)
t = threading.Thread(target=show)
t.start()
# Possible Output
# Thread-1


# 🔟 Main Thread
# Theory
# Every Python program starts with a main thread.
# Example
import threading
print(threading.current_thread().name)
# Output
# MainThread

"""11 Thread Lifecycle
    Thread states:
                New
                 ↓
                Runnable
                 ↓
                Running
                 ↓
                Waiting
                 ↓
                Terminated

12 Thread Synchronization
Theory
When multiple threads access the same resource, problems can occur.
To control this, Python provides Locks.
Example Using Lock
"""
import threading
lock = threading.Lock()
def task():
    lock.acquire()
    print("Thread running")
    lock.release()
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
"""
1️⃣3️⃣  Thread vs Process
        Feature	        Thread	    Process
        Memory	        Shared	    Separate
        Speed	        Faster	    Slower
        Communication	Easy	    Harder
"""

"""
Python process module:
multiprocessing

1️⃣4️⃣ Thread Example with Delay
    Example using:
    time
"""
import threading
import time
def task():
    for i in range(3):
        print("Running")
        time.sleep(1)

t = threading.Thread(target=task)
t.start()
"""
1️⃣5️⃣ Practical Use of Threads

Threads are used in:

Web servers
Chat applications
Download managers
Game engines
Background tasks

Many frameworks use threads internally like:

Django
Flask
🧠 Summary
Thread
   ↓
threading module
   ↓
Thread(target=function)
   ↓
start()
   ↓
join()
🎯 Key Points

✔ Thread is a lightweight process
✔ Threads share the same memory
✔ Python uses the threading module
✔ start() begins execution
✔ join() waits for completion

"""