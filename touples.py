mytuple = ()
print(type(mytuple))
print(id(mytuple))

dtuple = (1,2.3,"hello",True,8+7j)
print(type(dtuple))
print(id(dtuple))

print(dtuple)
print(dtuple[0])
print(id(dtuple[0]))
print(dtuple[0])
print(dtuple[1])
print(dtuple[2])
print(dtuple[3])
print(dtuple[4])

var = 0
while var < 5:
    print(dtuple[var])
    var += 1

for i in dtuple:
    print(i)

for i in range(0,5,1):
    print(dtuple[i])

print(dtuple[::-1])
print(dtuple[0:])
print(dtuple[1:])
print(dtuple[:1])
print(dtuple[:2])
print(dtuple[0:2])
print(dtuple[1:2])

len = len(dtuple)
print(len)
while len > 0:
    print(dtuple[len-1])
    len -= 1

for  i in range(4,-1,-1):
    print(dtuple[i])

print(dtuple[::-1])

dtuple.count("a")
print(dtuple)
print(dtuple.index(2.3))
dtuple = (1,1,1,"hello",8+7j)
print(dtuple.count(1))
dtuple = (1,1,1,"hello",True,8+7j)
print(dtuple.count(1))
tuple2 = (1,2,3,4,5,6,7,8,9,10)
# print(tuple + tuple2) // error cant combine

