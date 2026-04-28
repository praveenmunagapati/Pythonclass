# ============================================
# PYTHON COMPLETE CODE-FIRST MASTER FILE
# ============================================

# ----------- KEYWORDS DEMO -----------
# False, None, True, and, as, assert, async, await,
# break, class, continue, def, del, elif, else, except,
# finally, for, from, global, if, import, in, is, lambda,
# nonlocal, not, or, pass, raise, return, try, while, with, yield

# ----------- VARIABLES & TYPES -----------
a = 10              # int
b = 10.5            # float
c = 2 + 3j          # complex
d = "hello"         # string
e = True            # boolean

# ----------- TYPE CHECKING -----------
print(type(a), type(b), type(c), type(d), type(e))

# ----------- TYPE CASTING -----------
x = int(10.9)
y = float(5)
z = str(100)

# ----------- OPERATORS -----------

# Arithmetic
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)

# Comparison
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(10 <= 5)

# Logical
print(True and False)
print(True or False)
print(not True)

# Assignment
a = 5
a += 2
a -= 1
a *= 3
a /= 2

# Identity
a = [1,2]
b = [1,2]
print(id(a),id(b))
print(a is b)
print(a is not b)

# Membership
print(1 in [1,2,3])
print(4 not in [1,2,3])

# Bitwise
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)

# ----------- STRINGS -----------
s = "hello"
print(s.upper())
print(s.lower())
print(s.replace("h", "H"))
print(s.split("e"))

# ----------- LIST -----------
lst = [1,2,3]
lst.append(4)
lst.extend([5,6])
lst.insert(1, 99)
lst.remove(2)
lst.pop()
print(lst)

# ----------- TUPLE -----------
t = (1,2,3)
print(t[0])

# ----------- SET -----------
s = {1,2,3}
s.add(4)
s.remove(2)
print(s)

# ----------- DICTIONARY -----------
d = {"a":1, "b":2}
d["c"] = 3
print(d.keys())
print(d.values())
print(d.items())

# ----------- CONTROL FLOW -----------

# IF
num = 10
if num > 5:
    print("Greater")
elif num == 5:
    print("Equal")
else:
    print("Smaller")

# FOR LOOP
for i in range(3):
    print(i)

# WHILE LOOP
i = 0
while i < 3:
    print(i)
    i += 1

# BREAK, CONTINUE, PASS
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    pass
    print(i)

# ----------- FUNCTIONS -----------

def add(a, b):
    return a + b

print(add(2,3))

# DEFAULT PARAM
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Yo")

# *args
def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4))

# **kwargs
def show(**kwargs):
    print(kwargs)

show(name="Yo", age=25 , gender = 'male')

# LAMBDA
square = lambda x: x*x
print(square(5))

# ----------- COMPREHENSIONS -----------

# LIST
lst = [x*x for x in range(5)]

# SET
st = {x for x in range(5)}

# DICT
dc = {x: x*x for x in range(5)}

# ----------- EXCEPTION HANDLING -----------

try:
    x = int("abc")
except ValueError:
    print("Error")
finally:
    print("Done")

# RAISE
def check(n):
    if n < 0:
        raise ValueError("Negative")

# ----------- FILE HANDLING -----------

with open("file.txt", "w") as f:
    f.write("Hello")

with open("file.txt", "r") as f:
    print(f.read())

# ----------- OOP -----------

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

p = Person("Yo")
p.show()

# INHERITANCE
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

Dog().speak()

# ENCAPSULATION
class Bank:
    def __init__(self):
        self.__bal = 0

    def deposit(self, amt):
        self.__bal += amt

    def get(self):
        return self.__bal

b = Bank()
b.deposit(100)
print(b.get())

# ----------- ITERATOR -----------

lst = [1,2,3]
it = iter(lst)
print(next(it))

# ----------- GENERATOR -----------

def gen(n):
    for i in range(n):
        yield i

for i in gen(3):
    print(i)

# ----------- DECORATOR -----------

def deco(func):
    def wrap():
        print("Before")
        func()
        print("After")
    return wrap

@deco
def hello():
    print("Hello")

hello()

# ----------- MODULE IMPORT -----------

import math
print(math.sqrt(16))

from math import pi
print(pi)

# ----------- GLOBAL / NONLOCAL -----------

x = 10

def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
    inner()
    print(x)

outer()

# ----------- ASSERT -----------

assert 2 + 2 == 4

# ----------- ASYNC / AWAIT -----------

import asyncio

async def task():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(task())

# ----------- DEL -----------

x = 10
del x

# ----------- WITH -----------

with open("file.txt") as f:
    data = f.read()

# ----------- YIELD FROM -----------

def sub():
    yield 1
    yield 2

def main():
    yield from sub()

for i in main():
    print(i)

# ============================================
# END OF MASTER FILE
# ============================================

# ============================================================
# PYTHON INTERNALS / ADVANCED BEHAVIOR MASTER FILE
# ============================================================

# ---------------- MEMORY MODEL ----------------
# Python uses:
# - Stack (function calls, references)
# - Heap (actual objects)
# Variables store REFERENCES to objects, not values

a = 10
b = a

print(id(a), id(b))  # same object (immutable reuse)

b = 20
print(id(a), id(b))  # different now


# ---------------- MUTABILITY TRAP ----------------
# Mutable objects change in-place

lst1 = [1, 2, 3]
lst2 = lst1

lst2.append(4)

print(lst1)  # changed! (same reference)


# ---------------- COPY BEHAVIOR ----------------
import copy

a = [[1,2], [3,4]]

b = a              # reference
c = copy.copy(a)   # shallow copy
d = copy.deepcopy(a)  # deep copy

a[0][0] = 99

print(b)  # affected
print(c)  # affected (shallow)
print(d)  # safe


# ---------------- SMALL INTEGER CACHING ----------------
# Python caches small integers (-5 to 256)

x = 100
y = 100

print(x is y)  # True (cached)


# ---------------- STRING INTERNING ----------------
s1 = "hello"
s2 = "hello"

print(s1 is s2)  # often True


# ---------------- BYTECODE INSPECTION ----------------
import dis

def add(a, b):
    return a + b

dis.dis(add)  # see Python bytecode


# ---------------- FUNCTION OBJECT INTERNALS ----------------
def func(a, b=10):
    return a + b

print(func.__code__.co_varnames)
print(func.__defaults__)


# ---------------- CLOSURE ----------------
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
print(f(5))  # closure retains x


# ---------------- GIL DEMO ----------------
# CPU-bound threads don't scale due to Global Interpreter Lock

import threading
import time

def cpu_task():
    count = 0
    for _ in range(10_000_000):
        count += 1

start = time.time()

t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

t1.start()
t2.start()

t1.join()
t2.join()

print("Threads Time:", time.time() - start)


# ---------------- MULTIPROCESSING (TRUE PARALLEL) ----------------
from multiprocessing import Process

start = time.time()

p1 = Process(target=cpu_task)
p2 = Process(target=cpu_task)

p1.start()
p2.start()

p1.join()
p2.join()

print("Processes Time:", time.time() - start)


# ---------------- ASYNC EVENT LOOP ----------------
import asyncio

async def async_task():
    print("Start")
    await asyncio.sleep(1)
    print("End")

async def main():
    await asyncio.gather(async_task(), async_task())

asyncio.run(main())


# ---------------- ITERATOR PROTOCOL ----------------
class MyIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        else:
            raise StopIteration

for x in MyIter(3):
    print(x)


# ---------------- GENERATOR INTERNAL ----------------
def gen():
    yield 1
    yield 2

g = gen()
print(next(g))
print(next(g))


# ---------------- DESCRIPTOR PROTOCOL ----------------
# Controls attribute access

class Descriptor:
    def __get__(self, obj, objtype):
        return "Intercepted"

class Test:
    x = Descriptor()

t = Test()
print(t.x)  # calls __get__


# ---------------- __slots__ (MEMORY OPTIMIZATION) ----------------
class Fast:
    __slots__ = ['x']

    def __init__(self):
        self.x = 10

f = Fast()
print(f.x)


# ---------------- METACLASS ----------------
# Class that creates classes

class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['added'] = "Injected"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

m = MyClass()
print(m.added)


# ---------------- CUSTOM LIST IMPLEMENTATION ----------------
class MyList:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data += [val]

    def __getitem__(self, index):
        return self.data[index]

ml = MyList()
ml.append(10)
ml.append(20)

print(ml[0])


# ---------------- CONTEXT MANAGER ----------------
class MyContext:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Exit")

with MyContext():
    print("Inside")


# ---------------- RECURSION STACK ----------------
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))


# ---------------- MEMORY SIZE ----------------
import sys

a = [1,2,3]
print(sys.getsizeof(a))


# ---------------- DYNAMIC ATTRIBUTE ADDITION ----------------
class A:
    pass

obj = A()
obj.new_attr = 100

print(obj.new_attr)


# ---------------- EVAL / EXEC ----------------
code = "print(2 + 3)"
exec(code)

expr = "10 * 5"
print(eval(expr))


# ---------------- FINAL NOTE ----------------
# At this level, Python is:
# - object model driven
# - reference based
# - bytecode executed
# - constrained by GIL for threads
# - highly dynamic (runtime modification)

# ============================================================
# END
# ============================================================