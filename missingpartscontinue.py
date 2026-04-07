#Scope: LEGB Rule (Local, Enclosing, Global, Built-in).
c = 89
def foo():
    a = 56
    global  c
    c = 78

def main() :
    a = 10
    foo()
    #c = 56
    global  c
    c = 44
    foo()
    print(c)

main()

def foo():
    var = 1
    return var

def main():
    print(foo())
    print(foo())
    print(foo())
main()
var = 0
def foo():
    global var
    var = var + 1
    return var

def main():
    print(foo())
    print(foo())
    print(foo())
main()
#var = 0
def foo():
    # global var
    # var = var + 1
    # yield var
    yield 1
    yield 2
    yield 3

def main():
    myyeild = foo()
    print(type(myyeild))
    print(next(myyeild))
    print(next(myyeild))
    print(next(myyeild))
main()

var = 0
def foo():
    global var
    var = var + 1
    yield var

def main():
    print(next(foo()))
    print(next(foo()))
    print(next(foo()))
    print(next(foo()))
    print(next(foo()))
    print(next(foo()))
main()

# without global var
def incrementer(start=0):
    current = start
    while True:
        yield current
        current += 1

# Initialize the generator
gen = incrementer(start=1)

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
print(next(gen))  # Output: 5
print(next(gen))  # Output: 6
print(next(gen))  # Output: 7

def myrange(start=None,stop=None,step=1):
    current = start
    while current < stop:
        yield current
        current += step

mygen = myrange(0,5,1)
for i in mygen:
    print(i)
print("generator stoped")


