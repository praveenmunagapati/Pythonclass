"""
1️⃣ What is Asynchronous Programming?
Theory

Normally Python programs run synchronously:
Task1 → Task2 → Task3
Each task waits until the previous one finishes.
But sometimes tasks involve waiting:
Network requests
File downloads
API calls
Database queries

Instead of wasting time waiting, Python can run other tasks during the wait.
This is called Asynchronous Programming.
Example (Concept)
Synchronous execution:
Download File 1
(wait 5 sec)
Download File 2
(wait 5 sec)
Total time = 10 seconds

Asynchronous execution:
Download File 1
Download File 2
(wait together)
Total time ≈ 5 seconds

2️⃣ What is async?
Theory
The async keyword is used to define an asynchronous function.
These functions are called coroutines.
Syntax
async def function_name():
Example
"""
import asyncio
async def hello():
    print("Hello")
asyncio.run(hello())

# This function does not run immediately like normal functions.
# It must be executed using an event loop.
"""
3️⃣ What is await?
Theory
await is used inside an async function.
It tells Python:
"Pause this function and allow other tasks to run until 
the awaited task finishes."
Example
"""
import asyncio

async def task():
    print("Task started")
    await asyncio.sleep(2)
    print("Task finished")
asyncio.run(task())
# Output
# Task started
# (wait 2 seconds)
# Task finished
"""
4️⃣ Event Loop
Theory
An event loop manages asynchronous tasks.

It:
schedules tasks
runs them
switches between them when they wait

In Python we usually start it using:
asyncio.run()
Example
"""
import asyncio

async def main():
    print("Program started")
asyncio.run(main())
"""
5️⃣ Example: Two Async Tasks
Program
"""
import asyncio
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")
async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    await task1()
    await task2()

asyncio.run(main())
# Execution
# Task 1 started
# (wait)
# Task 1 finished
# Task 2 started
# (wait)
# Task 2 finished
# Tasks run sequentially here.

# 6️⃣ Running Tasks Concurrently
# To run tasks at the same time, use:
# asyncio.gather()
# Example
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Output
# Task 1 started
# Task 2 started
# (wait 2 seconds)
# Task 1 finished
# Task 2 finished

#Both tasks run concurrently.

# 7️⃣ Example: Async Download Simulation
# Program
import asyncio

async def download_file(name):
    print("Downloading", name)
    await asyncio.sleep(3)
    print(name, "downloaded")

async def main():
    await asyncio.gather(
        download_file("file1"),
        download_file("file2"),
        download_file("file3")
    )
asyncio.run(main())

# Output
# Downloading file1
# Downloading file2
# Downloading file3
# (wait)
# file1 downloaded
# file2 downloaded
# file3 downloaded
"""
8️⃣                 Async vs Threading
            Feature	            Async	    Threading
            Memory	            Low	        Higher
            Best for	        I/O tasks	CPU tasks
            Context switching	Fast	    Slower
            
9️⃣ Where Async is Used
Async programming is used in:
Web servers
APIs
Chat applications
Streaming services
High-performance networking
Popular frameworks using async:
FastAPI
aiohttp
Node.js (similar async concept)

🔟 Common Async Functions in Python
From the asyncio module:
asyncio.run()
asyncio.sleep()
asyncio.gather()
asyncio.create_task()
asyncio.wait()
"""
#1️⃣1️⃣ Example Using create_task

import asyncio
async def work():
    print("Working...")
    await asyncio.sleep(2)
    print("Done")
async def main():
    task = asyncio.create_task(work())
    await task

asyncio.run(main())
"""
1️⃣2️⃣ Async Flow Diagram
Program Start
      ↓
Event Loop
      ↓
Async Function
      ↓
await
      ↓
Other Task Runs
      ↓
Return to Original Task
🎯 Key Points for Students

✔ async defines asynchronous functions
✔ await pauses execution until task finishes
✔ asyncio manages async tasks
✔ Event loop controls scheduling
✔ Best used for I/O-bound tasks

🧠 Quick Comparison
Normal Function
def task():
    pass
Async Function
async def task():
    await something()
"""