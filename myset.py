set = {}
print(set)
print(id(set))
print(type(set))
set = {1,2,3,4,5,6,7,8,9,10}
print(set)
print(id(set))
print(type(set))

set = {1,2,3,4,5,2,5,10,9,7,6,2,3,1,6,7,8,9,10}
print(set)
print(id(set))
print(type(set))

#print(set[0]) error
#print(set[1])
# no index

for i in set:
    print(i)

set.add(11)
print(set)
set.pop()# first element
print(set)
# set.clear()
# print(set)
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {1,2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.issuperset(set2))
print(set1.difference(set2))
set1.clear()
print(set1)
