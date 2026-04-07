"""
What is Polymorphism?

    Poly = Many
    Morphism = Forms

    Same method name → Different behavior.

    Example:
    start() method works differently for Car, Bike, Bus.


Types of Polymorphism in Python

Python supports:
    Duck Typing (Dynamic Polymorphism)
    Method Overriding (Runtime Polymorphism)
    Operator Overloading
    Method Overloading (Simulated in Python)
    Function Polymorphism (Built-in functions)

"""
"""
1 Duck Typing (Most Important in Python)
Concept:
    “If it looks like a duck and quacks like a duck, it is a duck.”
    Python doesn’t care about object type — it cares about method presence.
"""

class CreditCard:
    def pay(self):
        print("Paid using Credit Card")

class UPI:
    def pay(self):
        print("Paid using UPI")

class Cash:
    def pay(self):
        print("Paid using Cash")

def make_payment(obj):
    obj.pay()   # Duck typing
"""
    No inheritance required
    No common parent required
    Python just checks if .pay() exists.
"""
#c = CreditCard()
make_payment(CreditCard())
make_payment(UPI())
make_payment(Cash())

class Payment:
    def pay(self):
        pass
class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")
class UPI(Payment):
    def pay(self):
        print("Paid using UPI")
class Cash(Payment):
    def pay(self):
        print("Paid using Cash")

Credit = CreditCard()
Credit.pay()
UPI = UPI()
UPI.pay()
Cash = Cash()
Cash.pay()

"""
    2.Method Overriding (Runtime Polymorphism)
        Child class modifies parent method.
"""
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):   # Overriding
        print("Car starts with key ignition")

v = Vehicle()
c = Car()
"""
    Same method name
    Different behavior
    Decided at runtime
"""
v.start()
c.start()
"""
    3.Operator Overloading
    Same operator behaves differently for different objects.
    Example:
        + adds numbers
        + joins strings
"""

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages
    def __sub__(self, other):
        return self.pages - other.pages
b1 = Book(100)
b2 = Book(200)

print(b1 + b2)
print(b2 - b1)

"""
Here + works for Book objects.
Common operator methods:

    __add__
    __sub__
    __mul__
    __str__
    __len__

"""
class Mylist:
    def __init__(self, list):
        self.list = list
    def __add__(self, other):
        return self.list + other.list

l1 = Mylist([1,2,3])
l2 = Mylist([4,5,6])
print(l1 + l2)


"""
4. Method Overloading (Simulated in Python)

    Python does NOT support true method overloading like Java.
    Instead, we use:
        Default arguments
        Variable arguments (*args)
"""
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    def addall(self, a, b=0, c=0,*args):
        total = a + b + c
        for arg in args:
            total = total + arg

        return total

calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.addall(10, 20, 30,40,50,60,70,80,90))

"""
Same method name → works differently.
"""

"""
5.Function Polymorphism (Built-in Functions)
Built-in functions work on multiple data types.

"""

print(len("Hello"))
print(len([1,2,3]))
print(len({1:10, 2:20}))

"""
len() works on:
    String
    List
    Dictionary
"""


def mylen(obj):
    if type(obj) == list:
        count = 0
        for x in obj:
            count += 1
        return count
    if type(obj) == tuple:
        count = 0
        for x in obj:
            count += 1
        return count
    if type(obj) == set:
        count = 0
        for x in obj:
            count += 1
        return count
    if type(obj) == dict:
        count = mylen(list(obj.keys()))
        return count


mylist = [1,2,3,4,5]
print("no of elements in list are {0}".format(mylen(mylist)))

mytuple = (1,2,3,4,5)
print("no of elements are in tuple are {0}".format(mylen(mytuple)))

mytuple = {1,2,3,4,5}
print("no of elements are in tuple are {0}".format(mylen(mytuple)))


myset = {1,2,3,4,5}
print("no of elements are in set are {0}".format(mylen(myset)))

mydict = {"a":1,"b":2,"c":3}
print("no of key values  in dictionary are {0}".format(mylen(mydict)))


