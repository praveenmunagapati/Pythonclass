mydict = {}
print(mydict)
print(id(mydict))
print(type(mydict))

mydict = {"prerana":2,3:4,5:6,"prerana":2}# no duplicates
print(mydict)
print(id(mydict))
print(mydict["prerana"])
print(mydict[3])
print(mydict[5])

for key,value in mydict.items():
    print(key,value)

a,b = [1,3]#destructuring
print(a,b)
for i in mydict.keys():
    print(i)
for i in mydict.values():
    print(i)
print(len(mydict))

print(mydict.get(3))
mydict.pop("prerana")
print(mydict)
mydict["prerana"] = 3
print(mydict)
del mydict["prerana"]
print(mydict)

mydict.clear()
print(mydict)
