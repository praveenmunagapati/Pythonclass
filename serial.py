"""

Serialization in Python means converting a Python object into
a format that can be stored or transmitted
(like a file, database, or network).
Later, the data can be reconstructed back into
the original object using deserialization.

    What is Serialization?

    Serialization → Convert object → Storable format
    Deserialization → Convert back → Python object

    Example:

    Python Object
          ↓
    Serialization
          ↓
    File / Network / Database
          ↓
    Deserialization
          ↓
    Python Object

Why Serialization is Needed
Common uses:
    Saving program state
    Sending objects over network
    Caching
    Machine learning models
    Distributed systems
    APIs and microservices

Example:
    Save a trained ML model and load it later.


Types of Serialization in Python

Main approaches:
    Pickle (binary serialization)
    JSON serialization
    Marshal
    Shelve
    Custom serialization

"""
"""
Pickle Serialization
    pickle converts Python objects into binary byte streams.
    Works with:
        Lists
        Dictionaries
        Classes
        Objects
        
"""
#Example: Serialize Object
import pickle
data = {"name": "Ravi", "age": 25}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)


#Deserialize Object
import pickle
with open("data.pkl", "rb") as file:
    data = pickle.load(file)
print(data)

#Serializing Class Objects
import pickle
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Ravi", 90)

with open("student.pkl", "wb") as file:
    pickle.dump(s1, file)

#Deserialize Class Object
import pickle
with open("student.pkl", "rb") as file:
    s = pickle.load(file)
print(s.name)
print(s.marks)


"""
JSON Serialization
JSON is text-based and widely used for APIs.
    Works with:
        dict
        list
        string
        int
        float
        boolean
"""
#Convert Python → JSON
import json
data = {"name": "Ravi", "age": 25}
json_data = json.dumps(data)
print(json_data)


#JSON → Python
import json
json_string = '{"name":"Ravi","age":25}'
data = json.loads(json_string)
print(data["name"])


#Writing JSON File
import json
data = {"name":"Ravi","age":25}
with open("data.json","w") as file:
    json.dump(data,file)

#Reading JSON File
import json
with open("data.json") as file:
    data = json.load(file)
print(data)

"""
Marshal Serialization
Used internally by Python.
Used for:
.pyc compiled files
Example:
"""

import marshal
data = [1,2,3,4]
serialized = marshal.dumps(data)
print(serialized)

#Deserialize
data = marshal.loads(serialized)
print(data)

#Not safe for general use.

"""
Shelve Serialization
shelve works like a persistent dictionary.
Example
"""
import shelve
db = shelve.open("mydata")
db["name"] = "Ravi"
db["age"] = 25
db.close()

#Read

import shelve
db = shelve.open("mydata")
print(db["name"])
db.close()

"""Custom Serialization

You can define how objects are serialized.
Example:
"""
import json

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def to_dict(self):
        return {"name":self.name,"marks":self.marks}

s=Student("Ravi",90)
json_data=json.dumps(s.to_dict())
print(json_data)

"""
Pickle Protocols
Pickle supports multiple protocols.
Example

    pickle.dump(obj,file,protocol=pickle.HIGHEST_PROTOCOL)
    Higher protocol → faster & smaller files.

Security Warning
Never unpickle data from untrusted sources

Because pickle can execute arbitrary code.
Safer alternatives:
JSON
Protobuf
MessagePack

Serialization Comparison
    Method	    Format	    Use
    Pickle	    Binary	    Python objects
    JSON	    Text	    APIs, web
    Marshal	    Binary	    Python internals
    Shelve	    File DB	    Persistent storage

Real-World Uses
    Serialization is used in:
    Machine learning model saving
    REST APIs
    Distributed computing
    Caching systems
    Message queues
    Database storage

Simple Visualization

        Python Object
             ↓
        pickle/json.dumps
             ↓
        Serialized Data
             ↓
        pickle/json.loads
             ↓
        Python Object

One-line definition for exams/interviews
    Serialization is the process of converting 
    a Python object into a byte stream or text format so 
    that it can be stored or transmitted and later reconstructed.
"""