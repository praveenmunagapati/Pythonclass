class Animal:
    def __init__(self):
        print("Animal constructor")
        self.breathes = True

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog constructor")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat constructor")

d = Dog()
c = Cat()

print("Cat constructor")

class Device:
    def __init__(self):
        print("Device constructor")
        self.year = True

class Phone(Device):
    def __init__(self):
        super().__init__()
        print("Phone constructor")

class Camera(Device):
    def __init__(self):
        super().__init__()
        print("Camera constructor")

class SmartPhone(Phone, Camera):
    def __init__(self):
        super().__init__()  # Follows MRO
        print("SmartPhone constructor")

sp = SmartPhone()

print(SmartPhone.mro())

n = 2.8
p = float(2.8)
print(n)
print("hi"[0])

