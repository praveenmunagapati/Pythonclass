"""

Python Exception Handling is used to handle
runtime errors gracefully
so that your program doesn’t crash unexpectedly.
Let’s cover everything from basics to advanced,
with examples.

    What is an Exception?
    An exception is an error that occurs during program execution.

"""
print(10 / 0)
"""
    Output
    ZeroDivisionError: division by zero

    This stops the program.

    Why Exception Handling?
        Without handling:
        Program crashes ❌
        Poor user experience ❌

        With handling:
        Program continues ✅
        Controlled error messages ✅
 """

"""
    3   Basic try-except
    Syntax
    try:
        # risky code
    except:
        # handle error
    Example
"""
try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Error occurred")
"""
    4.Handling Specific Exceptions
    Better to catch specific errors.
"""
try:
    num = int(input("Enter number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
"""
    5 Multiple Exceptions in One Line
"""
try:
    x = int("abc")

except (ValueError, TypeError):
    print("Error occurred")
"""
 6.else Block
    Runs if no exception occurs.
"""
try:
    x = int("10")
except:
    print("Error")
else:
    print("No error")

"""
    7 finally Block
    Runs always, whether error occurs or not.
"""
try:
    file = open("data.txt")
except:
    print("File not found")
finally:
    print("Closing program")
"""
8 Full Structure
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
"""

"""
    9 Raising Exceptions (raise)
    You can manually raise errors.
"""

age = 15
if age < 18:
    raise Exception("Not eligible")
"""
    10.Custom Exceptions
    Create your own exception class.
"""

class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong")
except MyError as e:
    print(e)
"""

11.Exception Hierarchy (Important)
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── Exception
      ├── ArithmeticError
      │     ├── ZeroDivisionError
      ├── ValueError
      ├── TypeError
      ├── IndexError
      ├── KeyError
      ├── FileNotFoundError
"""

"""
12.Common Exceptions
Exception	Example
ZeroDivisionError	10/0
ValueError	int("abc")
TypeError	"a" + 5
IndexError	list[10]
KeyError	dict["x"]
FileNotFoundError	open("no.txt")
"""

"""
13.Accessing Exception Object
"""

try:
    x = int("abc")
except ValueError as e:
    print("Error:", e)
"""
14.Nested try-except
"""

try:
    try:
        print(10/0)
    except ZeroDivisionError:
        print("Inner exception")
except:
    print("Outer exception")
"""
15.User-Defined Error with Logic
"""

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be >= 18")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)
"""
16 Using Exception with Files
"""

try:
    with open("data.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

"""
17.Assertions
Used for debugging.
"""

x = 5
assert x > 10, "x should be greater than 10"

"""

18 Best Practices

✔ Catch specific exceptions
✔ Avoid bare except:
✔ Use finally for cleanup
✔ Use custom exceptions for clarity
✔ Don’t suppress errors silently

"""

"""
19 Real-World Example
Banking System
"""

class InsufficientBalance(Exception):
    pass

balance = 1000

try:
    withdraw = 2000
    if withdraw > balance:
        raise InsufficientBalance("Not enough money")
    balance -= withdraw
except InsufficientBalance as e:
    print(e)

"""
20 Flow Diagram
try
 ↓
Error?
 ↓        ↓
Yes       No
 ↓         ↓
except     else
 ↓
finally (always runs)
"""

"""
Interview One-Liners

✔ Exception → runtime error
✔ try → risky code
✔ except → handle error
✔ else → runs if no error
✔ finally → always executes
✔ raise → manually throw error

"""
