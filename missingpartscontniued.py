names = ["Alice", "Bob"]
ids = [101, 102]
combined = list(zip(names, ids))  # [('Alice', 101), ('Bob', 102)]
print(combined)
myenum = enumerate(names)
for i, value in myenum:
    print(i, value)

nums = [1, 2, 3, 4, 5]

# Square every number
squared = list(
    map(lambda x: x ** 2,
        nums))  # [1, 4, 9, 16, 25]
print(squared)
# Keep only even numbers
evens = list(
    filter(lambda x: x % 2 == 0, nums))  # [2, 4]\
print(evens)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def foo(nums):
    return nums%2 == 0
evens = list(filter(foo, nums))
print(evens)
print(ord("A"))  # 65
print(chr(66))  # "B"
alphabet = [chr(i) for i in range(97, 123)]
print(alphabet)
alphabet = [chr(i) for i in range(65, 91)]
print(alphabet)

asciitable = [chr(i) for i in range(0, 255)]
print(asciitable)

colors = ["red", "green", "blue"]
it = iter(colors)

print(next(it)) # "red"
print(next(it)) # "green"
print(next(it)) # blue
# next(it) would give "blue", then the next would raise StopIteration

colors = "blue"
it = iter(colors)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

