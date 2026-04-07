import mymodule

inc = mymodule.incrementer(1)
print(next(inc))  # Output: 1
print(next(inc))  # Output: 2
print(next(inc))   # Output: 3

from mymodule import incrementer
inc = incrementer(1)
print(next(inc))  # Output: 1
print(next(inc))  # Output: 2
print(next(inc))   # Output: 3

import math
print(math.pi)
print(math.e)
print(math.pow(2,5))
print(math.log(2,5))
from math import floor
print(floor(1.5))
print(math.ceil(1.5))

from string import digits
print(digits)

print("hi " * 40)
#progression

for i in range(1,6,1):
    print(i)

for i in range(5,0,-1):
    print(i)

for i,j in enumerate(range(5,0,-1)):
    print(str(j) * (i+1))

for i,j in enumerate(list(range(5,0,-1))):
    print(str(j) * (i+1))
num = 10
for i,j in enumerate(list(range(num,0,-1))):
    print(str(j) * (i+1))

num = int (input("Enter a number: "))

for i,j in enumerate(list(range(num,0,-1))):
    print(str(j) * (i+1))

for i,j in enumerate(range(5,0,-1),start=1):
    print(str(j) * (i+1))