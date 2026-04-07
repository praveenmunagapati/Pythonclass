"""
Python File Operations allow programs to create, read, write, append, and manage files stored on disk. This is essential for data storage, logs, configuration files, datasets, etc.
I'll cover everything step-by-step.
What is File Handling in Python?
File handling means reading data from files or writing data to files.
Example real-world files:
    Text files (.txt)
    CSV files (.csv)
    JSON files (.json)
    Logs
    Data sets
Example path:
    data.txt

Opening a File
    Python uses the open() function.

    Syntax
    file_object = open("filename", "mode")

    Example:
    file = open("data.txt", "r")

"""
#file = open("data.txt", "r")
"""
File Modes
    Mode	Meaning
    r	    Read file
    w	    Write file (overwrite)
    a	    Append to file
    x	    Create new file
    t	    Text mode
    b	    Binary mode
    r+	    Read and write
    w+	    Write and read

"""
file = open("newfile.txt","x")
file.write("New File Created")
file.close()

file = open("data.txt", "w")
file.write("Hello World\n")
file.write("Python Programming\n")
file.close()

file = open("data.txt", "a")
file.write("Hello World\n")
file.write("Python Programming\n")
file.close()

file = open("data.txt", "r")
print(file.read()) #total file data loads into buffer
file.close()

file = open("data.txt", "r")
print(file.readline()) #loads one line at a time
print(file.readline()) #loads one line at a time
print(file.readline()) #loads one line at a time
print(file.readline()) #loads one line at a time
file.close()


file = open("data.txt", "r")
for line in file:
    print(line)
file.close()

#modifying file content
file = open("data.txt", "r")
content = file.read()
print(type(content))
print(content)
content = content.replace("Hello", "Hi")
print(type(content))
print(content)
file.close()

file = open("data.txt", "w")
file.write(content)
file.close()

with open("data.txt", "r") as file:
    data = file.read()
    print(data)

with open("FotoJet.jpg","rb") as f1:
    data = f1.read()
    #print(data)
with open("copy.jpg","wb") as f2:
    f2.write(data)

import os
if os.path.exists("newfile.txt"):
    print("File exists")
else:
    file = open("newfile.txt","x")
    file.write("New File Created")
    file.close()

import os
os.remove("newfile.txt")

import os
os.rename("data.txt","newdata.txt")

file = open("newdata.txt","w")
print(file.name)
print(file.mode)
print(file.closed)
file.close()

with open("newdata.txt") as file:
    for line in file:
        print(line.strip())

"""
CSV 
    newdata.txt
    name,age
    Ravi,25
    Priya,22

"""
import csv
with open("newdata.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
Working with JSON Files

Example JSON
data.json
    {
     "name": "Ravi",
     "age": 25
    }

"""
import json
with open("data.json") as file:
    data = json.load(file)

print(data["name"])
print(data["age"])