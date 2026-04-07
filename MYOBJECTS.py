#OOPS
#class
#object
"""
struct Student {
    int roll;
    char name[50];
    float marks;
};
"""
import email


class Student:
    # Correct constructor name
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

s1 = Student(101, "Praveen", 82.5)
print(s1.rollno)
print(s1.name)
print(s1.marks)
print(id(s1))
print(type(s1))

# Define a class (Blueprint)
class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    # Method to display details
    def display_details(self):
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Method to calculate grade
    def calculate_grade(self):
        if self.marks >= 75:
            print("Grade: A")
        elif self.marks >= 50:
            print("Grade: B")
        else:
            print("Grade: C")


# Object creation
s1 = Student(101, "Praveen", 82.5)

# Method calls
s1.display_details()
s1.calculate_grade()


class empty:
    pass
#empty class
e = empty()
print(id(e))
print(type(e))

class construct:
    def __init__(self):
        print("default Constructor")

d = construct()
print(id(d))
print(type(d))

class foo:
    def __init__(self, name):
        self.name = name
    def details(self):
        print(self.name)
    def __del__(self):
        print("Object destroyed")


f = foo("raj")
print(id(f))
print(type(f))
f.details()

"""
    4 pillars of oops
    encapsulation
    inheritance
    polymorphism 
    and abstraction
"""


class student:
    def __init__(self, name, roll, marks,age,gender,height,section,department,phoneno,bloodgroup,email,cgpa,mothername,fathername,address):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.age = age
        self.gender = gender
        self.height = height
        self.section = section
        self.department = department
        self.phoneno = phoneno
        self.bloodgroup = bloodgroup
        self.email=email
        self.cgpa = cgpa
        self.mothername = mothername
        self.fathername = fathername
        self.address = address


class teacher:
    def __init__(self, name,age,gender,height,department,phoneno,bloodgroup,email,mothername,fathername,address,experience,adhaar,salary):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender
        self.height = height
        self.department = department
        self.phoneno = phoneno
        self.bloodgroup = bloodgroup
        self.email = email
        self.mothername = mothername
        self.fathername = fathername
        self.address = address
        self.experience = experience
        self.adhaar = adhaar
        self.salary = salary




class person:
    def __init__(self, fathername):
        # def __init__(self, name, age, gender, height, department, phoneno, bloodgroup, email, mothername, fathername,
        #              address, experience, adhaar, salary):
        # self.name = name
        # self.id = id
        # self.age = age
        # self.gender = gender
        # self.height = height
        # self.department = department
        # self.phoneno = phoneno
        # self.bloodgroup = bloodgroup
        # self.email = email
        # self.mothername = mothername
        self.fathername = fathername
        # self.address = address




class student (person):
    def __init__(self, roll, marks,section,cgpa):
        super().__init__(fathername="ram charan")
        self.roll = roll
        self.marks = marks
        self.section = section
        self.cgpa = cgpa
archana = student(12,58,"A",7.5)
print(id(archana))
print(type(archana))
archana.fathername = "ramcharan"

print(archana.fathername)



class a:
    def __init__(self):
        print("a constructor")
class b(a):
    def __init__(self):
        super().__init__()
        print("b constructor")

b = b()
print(id(b))
print(type(b))


class a:
    def __init__(self,x,y):
        print("a constructor")
        self.x = x
        self.y = y

class b(a):
    def __init__(self,x,y,z):
        print("b constructor")
        super().__init__(x,y)
        self.z = z

b = b(10,20,30)
print(b.x)
print(b.y)
print(b.z)

class a:
    def __init__(self,x,y):
        print("a constructor")
        self.x = x
        self.y = y

class b(a):
    def __init__(self,x,y,z):
        print("b constructor")
        super().__init__(x,y)
        self.z = z

class c(b):
    def __init__(self,x,y,z,v):
        print("c constructor")
        super().__init__(x,y,z)
        self.v = v

c = c(10,20,30,40)
print(c.x)
print(c.y)
print(c.z)
print(c.v)

class a:
    def __init__(self,x,y):
        print("a constructor")
        self.x = x
        self.y = y

class b:
    def __init__(self,z):
        print("b constructor")
        self.z = z

class c(b,a):
    def __init__(self, x, y, z, v):
        self.v = v
        # self.__init__(z)
        b.__init__(self,z)
        a.__init__(self,x,y)

c = c(10,20,30,40)
print(c.x)
print(c.y)
print(c.z)
print(c.v)

class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
obj = B()
obj.show()

print(issubclass(B,A))
