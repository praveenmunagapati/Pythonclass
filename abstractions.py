"""
    In Python, Abstraction means
    "hiding implementation details and
    showing only essential features"
    to the user.


Example:
    When you drive a car, you only use steering, brake, accelerator.
    You don't need to know the engine mechanism.

Types of Abstraction in Python

    Python mainly supports two types of abstraction:

    1 Data Abstraction
    2 Control Abstraction

    And in implementation we usually use:

    3 Abstract Classes (ABC)
    4 Interfaces-like abstraction

"""
"""1️ Data Abstraction

Data abstraction hides internal data and exposes only required operations.

Example: Bank Account
        User can deposit/withdraw, but cannot directly modify balance.

"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(200)
acc.__balance = 50000
print(acc.get_balance())


"""
✔ Balance is hidden
✔ Access only through methods
# """
"""
2️⃣ Control Abstraction

Control abstraction hides complex logic inside functions.
Example:
    Car start system
    Driver presses start button → complex engine process happens internally.
"""

def start_car():
    check_fuel()
    check_engine()
    ignite_engine()
    print("Car started")

def check_fuel():
    print("Fuel check complete")

def check_engine():
    print("Engine check complete")

def ignite_engine():
    print("Engine ignition")

start_car()

"""

3 Abstract Classes (Using ABC Module)

Python provides abstraction using Abstract Base Classes.

    Module used:
        abc
    Key components:
        ABC
        abstractmethod

"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def foo(self):
        return 3.14 * 5 * 5

class Rectangle(Shape):

    def area(self):
        return 10 * 5

c = Circle()
r = Rectangle()

print(c.area())
print(r.area())

"""
Important Rule
You cannot create object of abstract class.
Shape()  X Error
"""

"""
    4 Interface-like Abstraction in Python
    Python does not have strict interfaces like Java,
    but abstract classes behave like interfaces.
    Example: Payment System
"""
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")

p1 = CreditCard()
p1.pay(500)

p2 = UPI()
p2.pay(300)

# """
# | Type                | Description                      | Example        |
# | ------------------- | -------------------------------- | -------------- |
# | Data Abstraction    | Hide internal data               | BankAccount    |
# | Control Abstraction | Hide complex logic               | start_car()    |
# | Abstract Class      | Base class with abstract methods | Shape          |
# | Interface-like      | Contract for classes             | Payment system |
#
# ✔ Abstraction focuses on what to do
# ✔ Encapsulation focuses on how it is done
# Example:
#
# Abstraction → Drive Car
# Encapsulation → Engine mechanism hidden
#
#"""