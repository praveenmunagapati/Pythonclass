# ==========================================
# PYTHON INTRODUCTORY WORKSHOP - MASTER FILE
# ==========================================

# --- SECTION 1: COMMENTS & BASIC SYNTAX ---
# This is a single-line comment. The computer ignores this text.

'''
This is a multi-line comment (or docstring).
It is used when your explanation spans multiple lines.
'''

print("--- 1. OUTPUT & SYNTAX ---")
print("Welcome to Python Class!")  # The print() function sends text to the screen.
print("-" * 30) # Formatting trick: This prints the dash 30 times.


# --- SECTION 2: VARIABLES, KEYWORDS & DATATYPES ---
print("\n--- 2. VARIABLES & DATA TYPES ---")

# Variables are containers for storing data values.
# Keywords (like True, False, None, if) are reserved and cannot be used as variable names.

# 1. String (str): Text enclosed in quotes
student_name = "Alex"

# 2. Integer (int): Whole numbers
student_age = 20

# 3. Float (float): Decimal numbers
test_score = 95.5

# 4. Boolean (bool): True or False logic
is_enrolled = True

# displaying the values and their 'Type'
print("Name:", student_name, " | Type:", type(student_name))
print("Age:", student_age, "   | Type:", type(student_age))
print("Score:", test_score, "| Type:", type(test_score))
print("Enrolled:", is_enrolled, "| Type:", type(is_enrolled))


# --- SECTION 3: INPUT & OUTPUT ---
print("\n--- 3. INPUT & OUTPUT ---")

# The input() function pauses the program and waits for the user to type.
# IMPORTANT: input() always returns a STRING.
user_name = input("Please enter your name: ")
user_fav_num = input("Enter your favorite number: ")

print("You entered:", user_name)
print("Raw number input:", user_fav_num)


# --- SECTION 4: TYPE CASTING ---
print("\n--- 4. TYPE CASTING ---")
# Type casting is converting data from one type to another.

# Converting the string input to an integer to do math
number_int = int(user_fav_num)
result = number_int + 10

# Converting a float to an int (removes decimal)
score_as_int = int(test_score)

# Converting a number to a string (for concatenation)
age_string = str(student_age)

print(f"Your number {number_int} + 10 = {result}")
print(f"Original score: {test_score} -> Casted to int: {score_as_int}")


# --- SECTION 5: FORMATTING STRINGS ---
print("\n--- 5. STRING FORMATTING ---")
# formatting allows us to mix variables and text cleanly.

# Method 1: f-Strings (Fastest & Modern Way) - Recommended
print(f"Hello {user_name}, your score is {test_score}.")

# Method 2: .format() (Older method)
print("Student: {}, Age: {}".format(user_name, student_age))

# Method 3: Comma separation (Simplest)
print("Student:", user_name, "is enrolled:", is_enrolled)

print("\n--- END OF PROGRAM ---")


a = 10
b = a
c = a
a = 6
print(id(a))
print(id(b))
print(id(c))

import copy

d = copy.deepcopy(a)
e = copy.deepcopy(a)
print(id(d))
print(id(e))



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
