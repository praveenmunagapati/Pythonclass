from operator import itemgetter

inventory = [("Apple", 10, 1.5), ("Banana", 5, 2.0), ("Cherry", 0, 5.0)]
print(inventory)
#Filter: Remove any items where the Quantity is 0 (they are out of stock).
inventory = [items for items in inventory if items[1]>0]
print(inventory)
#Transform: For the remaining items, .
# calculate the total value of that inventory (Quantity * Price_Per_Unit).
# Round the total value to 2 decimal places. Create a new list of tuples in the format: (Item_Name, Total_Value).
inventory = [(items[0], round(items[1] * items[2], 2)) for items in inventory]
print(inventory)
#Sort: Sort the new list in descending order based on the Total_Value.
inventory = sorted(inventory, key=itemgetter(1), reverse=True)
print(inventory)

#Tie-breaker: If two items have the exact same total value,
# sort them alphabetically by their Item_Name.
