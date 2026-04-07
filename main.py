"""
LeetCode-Style Problem Statement

Title: 1003. Inventory Value Analyzer

Difficulty: Medium

Description:
You are given a list of tuples representing a store's inventory. Each tuple contains three elements: (Item_Name, Quantity, Price_Per_Unit).
(Example: ("Apple", 10, 1.5) means there are 10 Apples, each costing $1.50).
Write a Python program that does the following:
Filter: Remove any items where the Quantity is 0 (they are out of stock).
Transform: For the remaining items, calculate the total value of that inventory (Quantity * Price_Per_Unit). Round the total value to 2 decimal places. Create a new list of tuples in the format: (Item_Name, Total_Value).
Sort: Sort the new list in descending order based on the Total_Value.
Tie-breaker: If two items have the exact same total value, sort them alphabetically by their Item_Name.
Function Signature:
class Solution:
    def processInventory(self, inventory: List[tuple]) -> List[tuple]:
        pass

Test Cases

case=1
input=[("Apple", 10, 1.5), ("Banana", 5, 2.0), ("Cherry", 0, 5.0)]
output=[('Apple', 15.0), ('Banana', 10.0)]

case=2
input=[("Milk", 2, 5.0), ("Bread", 5, 2.0)]
output=[('Bread', 10.0), ('Milk', 10.0)]

case=3
input=[("Desk", 5, 150.5), ("Chair", 20, 45.25), ("Lamp", 0, 15.0), ("Rug", 10, 90.5)]
output=[('Chair', 905.0), ('Rug', 905.0), ('Desk', 752.5)]

case=4
input=[("Zeta", 2, 10.0), ("Alpha", 4, 5.0), ("Beta", 1, 20.0)]
output=[('Alpha', 20.0), ('Beta', 20.0), ('Zeta', 20.0)]

case=5
input=[("Out_of_Stock_A", 0, 100.0), ("Out_of_Stock_B", 0, 50.0)]
output=[]

case=6
input=[]
output=[]

case=7
input=[("Pen", 1000, 1.25), ("Pencil", 2000, 0.50)]
output=[('Pen', 1250.0), ('Pencil', 1000.0)]

case=8
input=[("Oil", 3, 3.33)]
output=[('Oil', 9.99)]

case=9
input=[("Laptop", 1, 999.99), ("Mouse", 10, 25.5), ("Keyboard", 5, 50.0)]
output=[('Laptop', 999.99), ('Keyboard', 250.0), ('Mouse', 255.0)]

case=10
input=[("Water", 100, 0.99), ("Soda", 50, 1.98), ("Juice", 33, 3.0)]
output=[('Juice', 99.0), ('Soda', 99.0), ('Water', 99.0)]

"""

def processInventory(inventory):
    processed_list = []
    """
    Filter: Remove any items where the Quantity is 0 (they are out of stock).
    """
    inventory = [items for items in inventory if items[1] > 0]
    """
    Transform: For the remaining items, calculate the total value of that inventory 
    (Quantity * Price_Per_Unit). 
    Round the total value to 2 decimal places. 
    Create a new list of tuples in the format: (Item_Name, Total_Value).
    """
    inventory = [(items[0],round(items[1]*items[2],2)) for items in inventory ]

    return processed_list

if __name__ == '__main__':
    try:
        # Takes input from you and processes it the moment you press Enter
        raw_input = input().strip()
        
        if not raw_input:
            print("[]")
        else:
            # eval() safely turns your pasted text into a real list of tuples
            inventory = eval(raw_input)
            
            # Call the function
            result = processInventory(inventory)
            
            # Print the output exactly as expected
            print(result)
            
    except EOFError:
        pass
    except Exception as e:
        print("Error processing input:", e)


"""
How to test this in your IDE:
Run the code.
The console will wait for input. Paste Case 4:
[("Zeta", 2, 10.0), ("Alpha", 4, 5.0), ("Beta", 1, 20.0)]
Press Enter.
You will see them perfectly sorted alphabetically because 
their values tied at exactly 20.0:
[('Alpha', 20.0), ('Beta', 20.0), ('Zeta', 20.0)]
"""