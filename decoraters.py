"""
In Python, decorators like @abstractmethod are just functions that modify other functions.
So if you want to create your own decorator (like @abstractmethod),
you write a function that takes another function as input and returns a modified function.
I'll explain step-by-step.

1️⃣ Basic Idea of a Decorator
A decorator wraps a function.
"""
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


"""
@my_decorator

is equivalent to

say_hello = my_decorator(say_hello)

"""
"""
2️ How @abstractmethod Works Internally

@abstractmethod marks a function as abstract so that the subclass must implement it.

Simplified idea:
"""
def abstractmethod(func):
    func.__isabstractmethod__ = True
    return func
"""
Python’s ABCMeta later checks this flag.

3️⃣ Creating Your Own @abstractmethod (Simplified)

Example: Force subclasses to override a method.
"""
def my_abstractmethod(func):
    def wrapper(*args, **kwargs):
        raise NotImplementedError("Subclass must implement this method")
    return wrapper

class Animal:

    @my_abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()
d.sound()

"""
If a subclass does not implement it, calling it raises an error.
    4 Creating a Custom Decorator Like @log
      Example: Logging decorator.
"""
def log(func):

    def wrapper(*args, **kwargs):
        print("Function called:", func.__name__)
        result = func(*args, **kwargs)
        return result

    return wrapper

@log
def add(a, b):
    return a + b

print(add(3,4))

"""
5️⃣ Decorator with Parameters

You can also pass parameters.
"""
def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(30)
def greet():
    print("Hello")

greet()


""" 
    6 Real Structure of a Python Decorator
    
    decorator
       ↓
    function
       ↓
    wrapper
       ↓
    original function execution

Structure:
"""
def decorator(func):

    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result

    return wrapper
"""
    7 Example: Creating @require_login
"""

logged_in = False
def require_login(func):
    def wrapper(*args, **kwargs):
        if not logged_in:
            print("Login required")
            return
        return func(*args, **kwargs)

    return wrapper


@require_login
def view_profile():
    print("User profile")

view_profile()
"""

✔ Decorators are higher-order functions
✔ They wrap existing functions
✔ @decorator syntax is syntactic sugar
✔ Equivalent to
func = decorator(func)
"""
