def emptyfunc():
    pass

emptyfunc()
#sum = add(8,9) create function before calling
def add (a,b):
    return a+b

sum = add(5,6)
print(sum)
sum = add(5.5,6.4)
print(sum)
sum = add(5,6.4)
print(sum)
sum = add("HI ","HELLO")
print(sum)

# def sum(a,b,c):
#     return a+b+c
#
# sum = add(5,6,7)
# print(sum)
def default(a, b):
    return a+b
sum = default(4,6)
print(sum)
def default(a, b=6):
    return a+b
sum = default(4)
print(sum)

def default(a=5, b=6):#default parameters
    return a+b
sum = default()
print(sum)

#recursion
def factorial(n) :
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n - 1)
num = None
result = None
# num = int(input("enter a number"))
num = 5
if num < 0 :
    print("Factorial of a negative number is not possible.\\n");
else :
    result = factorial(num)
    print("The Factorial of {0} is {1}.".format(num, result))


def double(a):
    return a+a
doub = double(50)
print(doub)

doub = lambda a: a + a
print(doub(56))

sum = lambda a, b: a + b
print(sum(59,98))

def sum(a,*args):
    print(*args)
    for i in args:
        a = a + i
    return a
total = sum(0,1,2,3,4,5,6,7,8,9,10)
print(total)