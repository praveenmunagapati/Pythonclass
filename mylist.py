#lists
list = []
print(list)
print(id(list))
print(type(list))
list = [1,1.2,"hi",True,5+8j]
print(list)
print(list[0])
print(id(list[0]))
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

var = 0
while var < 5:
    print(list[var])
    var += 1

for i in list:
    print(i)

for i in range(0,5,1):
    print(list[i])

print(list[::-1])
print(list[0:])
print(list[1:])
print(list[:1])
print(list[:2])
print(list[0:2])
print(list[1:2])

list.insert(5,"extra")
print(list)
list.pop()
print(list)
# list.remove("hi")
# print(list)
slist = []
var = 0
for i in list:
    if i == "hi":
        continue
    slist.insert(var,i)
    var += 1
print(slist)
print(len(list))
print(type(list))
list = [89,54,21,77,1,5]
list.sort()
print(list)


list1 = [6,5,4]
list2 = ["hi",5.6,5]
print(list1+list2)
#print(list1-list2) // error no operator

# todo combine two lists without + or append
list1.append(list2)
print(list1)

for i in list1:
    print(i)

list1.reverse()
print(list1)

list1 = [6,5,4]
list2 = ["hi",5.6,5]
eleinlist1 = len(list1)
for i in list2:
    list1.insert(eleinlist1,i)
    eleinlist1 += 1

print(list1)

del list1
print(list1)
