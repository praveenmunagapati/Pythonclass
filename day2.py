#operators
var = 10
print(var)
print(type(var))
print(id(var))
var = 15.6
print(var)
print(type(var))
print(id(var))
var = "ram"
print(var)
print(type(var))
print(id(var))
var = True
print(var)
print(type(var))
print(id(var))
var = 5 + 5j
print(var)
print(type(var))
print(id(var))

var1 = 10;
print(var1)
print(type(var1))
print(id(var1))
# unsigned long long int a  = 1234567890111213141516171819
var = 1208925819614629174706176*1208925819614629174706176
print(var)
print(type(var))
print(id(var))

"""
    arthmetic + - / * %  // **
     assignment = ==  
    relational > < >= <= != 
    logical ops and or not
    bitwise & | ~ ^ << >> 
    in 
    is 
"""
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
print(a==b)
print(a!=b)
#print(a+=b) no shorthands
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print(type(a!=b))

print(True and True)
print(True and False)
print(False and True)
print(False and False)

isabig = a>b
print(isabig)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not False)
print(not True)

print(10&2)
# 1010 0010 & 0010
print(10|2)
# 1010 0010 | 1010

print(~0)
print(~1)
print(~2)
print(~3)
print(~-1)
print(~-2)
print(~-3)
print(~-4)

print(~-55345384810410481180851485010804454545)#no bounds
print(2<<3)
#10 < 33
# 10000

print(16>>3)
#16 10000 >> 3 -> 10
print(1>>2)
print(10 ^ 2)
# 10 1010 ^ 0010  -> 1000
# in
print(5 in [1,2,3,4,5,6,7])
print(50 in [1,2,3,4,5,6,7])
# is
print(var is a)

x = None
print(x)

# control statements
# if else
# while do for
#break goto continue

"""
c 
    if(condition){
        statements 1;
              statements 2;
            statements 3;
statements 4;
    }
python 
    suite of code
    if condition :
        statements 1
        statements 2
        statements 3
        statements 4
"""

if True:
    print("true")
    print("true")
    print("true")
    print("true")
if True:
 print("true")
 print("true")
 print("true")
 print("true")
 if False:
  print("true")
  print("true")
  print("true")
  print("true")
  # mind the indentation

a = 5
b = 6
c = 9

if a > b and a > c:
    print("a is big")
if b > a and b > c:
    print("b is big")
if c > a and c > b:
    print("c is big")

a = 5
b = 6
a,b = b,a
print(a)
print(b)

if False:
    print("true")
else:
    print("false")
b = 15
if a > b and a > c:
    print("a is big")
elif b > a and b > c:
    print("b is big")
elif c > a and c > b:
    print("c is big")

b = 9
if a > b and a > c:
    print("a is big")
elif b > a and b > c:
    print("b is big")
elif c > a and c > b:
    print("c is big")
else:
    print("None is big")

"""
    c 
    while(condition){
        statements 1;
        statements 2;
        }
    python 
     suite of code
     while condition :
         statements 1
         statements 2
         statements 3
       

"""

while False:
    print("none")
# while True:
#     print("Noooooo")

while False:
    print("none")
else:
    print("loop never enters")

for  i in range(1,101,2):
    print(i)
for  i in [9,8,7,6,5,4,3,2,1]:
    print(i)

