# terinary operator behaviour

# ? :
num = 7
if num % 2 == 0:
    print("even number")
else:
    print("odd")

result = "even" if num % 2 == 0 else "odd"
print(result)

# list comprehension
mylist = []
for i in range(2, 101, 2):
    mylist.append(i)
print(mylist)
# list
cmylist = [i for i in range(2, 101, 2)]
print(cmylist)

cmylist = [i for i in range(1, 101, 1) if i % 2 == 0]
print(cmylist)

cmylist = [i * i for i in range(1, 101, 1) if i % 2 == 0]
print(cmylist)
# tuple
cmylist = (i * i for i in range(1, 101, 1) if i % 2 == 0)
for i in cmylist:
    print(i)

cmylist = {i * i for i in range(1, 101, 1) if i % 2 == 0}
print(cmylist)

cmylist = {i: i * i for i in range(1, 101, 1) if i % 2 == 0}
print(cmylist.items())
print(cmylist.keys())
print(cmylist.values())

# match case
match num % 2 == 0:
    case True:
        print("even number")
    case False:
        print("odd number")

match num % 2 == 0:
    case 1:
        print("even number")
    case 0:
        print("odd number")

match result:
    case "even":
        print("even number")
    case "odd":
        print("odd number")

match num / 5:
    case 1.4 | 1.1666666666666667:
        print("1.4 or 1.1666666666666667")
    case None:
        print("none")

match result:
    case "even" if result == "even":
        print("even number")
    case "odd" if result == "odd":
        print("odd number")
num = 8
match result:
    case True if num % 2 == 0:
        print("even number")
    case False if num % 2 == 1:
        print("odd number")

# strings
name = "rani"
print(name)
print(type(name))
name = 'rani'
print(name)
print(type(name))
name = """
            rani 

                """
print(name)
print(type(name))

mystring = "hello world!"
print(mystring)
print(type(mystring))
for i in range(0, len(mystring)):
    print(mystring[i])

for i in mystring:
    print(i)

num = 6
result = "even" if num % 2 == 0 else "odd"
print("the number ", num, "is", result)
print("the number  {0} is  {1}.".format(num, result))
print(f"the number  {num} is  {result}")
# print(mystring[1:4])#string slicing
print(mystring[::-1])
print(mystring[:])
print(mystring[0:])
print(mystring[1:])
print(mystring[:6])
print(mystring[:7])
print(mystring[:13])
print(mystring[1:8])
print(mystring.capitalize())
print(mystring.title())
mystring = """In the modern digital era, understanding social structures is critical. SNA provides a lens to reveal hidden patterns behind complex social phenomena."""
print(mystring.replace(" ", ","))
mystring = "king"
print(mystring.upper())
mystring = "kInG"
print(mystring.lower())
print(mystring.find("k"))
print(mystring.find("n"))
mystring = """In the modern digital era, understanding social structures is critical. SNA provides a lens to reveal hidden patterns behind complex social phenomena."""
print(mystring.find("understanding"))
print(mystring.index("s"))
print(mystring.index("u"))
print(mystring.count("s"))
