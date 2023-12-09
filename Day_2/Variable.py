# Exercises: Level 1 Solution

# Day 2: 30 Days of Python Programming

# Declare first name variable and assign a value
first_name = "Olayinka"

# Declare last name variable and assign a value
last_name = "Babalola"

# Declare full name variable and assign a value
full_name = first_name + " " + last_name

# Declare country variable and assign a value
country = "Nigeria"

# Declare city variable and assign a value
city = "Lagos"

# Declare age variable and assign a value
age = 29

# Declare year variable and assign a value
year = 1994

# Declare is_married variable and assign a value
is_married = False

# Declare is_true variable and assign a value
is_true = False

# Declare is_light_on variable and assign a value
is_light_on = True

# Declare multiple variables on one line
x, y, z = 5, 10, 15

# Exercises: Level 2 Solution
# Checking data types of the variables using type() built-in function
print("Data types:")
print(type(first_name))        # <class 'str'>
print(type(last_name))         # <class 'str'>
print(type(full_name))         # <class 'str'>
print(type(country))           # <class 'str'>
print(type(city))              # <class 'str'>
print(type(age))               # <class 'int'>
print(type(year))              # <class 'int'>
print(type(is_married))        # <class 'bool'>
print(type(is_true))           # <class 'bool'>
print(type(is_light_on))       # <class 'bool'>
print(type(x))                 # <class 'int'>
print(type(y))                 # <class 'int'>
print(type(z))                 # <class 'int'>
print()

# Length of first name
length_of_first_name = len(first_name)
print("Length of first name:", length_of_first_name)
print()

# Compare length of first name and last name
compare_lengths = len(first_name) == len(last_name)
print("Are the lengths of first name and last name equal?", compare_lengths)
print()

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Arithmetic operations:")
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponential:", exp)
print("Floor Division:", floor_division)
print()

import numpy as np

# Circle calculations
radius_of_circle = 30

area_of_circle = np.pi * (radius_of_circle ** 2)
circum_of_circle = 2 * np.pi * radius_of_circle

print("Circle calculations:")
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)
print()

# User input
user_radius = float(input("Enter the radius of a circle: "))
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))
print()

# Reserved keywords
help('keywords')