# Task 1, declare your age as integer

Age = 29

# Task 2, decalre your height as float
Height = 5.6

# Task 3, declare a complex number 
complex_number = 3 + 2j

# Task 4, calculate the area of a triangle 

b = float(input("Enter base: "))
h = float(input("Enter height: "))
area = 0.5 * b * h
print(f"The area of the triangle is {area}")
print()

# Task 5, calaculate the perimeter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")
print()

# Task 6, calculate the width and length of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"Area: {area_rectangle}, Perimeter: {perimeter_rectangle}")
print()

# Task 7, calculate area of a circle 
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print(f"Area: {area_circle}, Circumference: {circumference}")
print()

# Task 8, calculate the slope,x and y intercept 
slope = 2
x_intercept = 2 / slope
y_intercept = -2
print(f"slope: {slope}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")
print()

#Task 9, find  the slope and euclidean distance 
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_formula = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"slope formula: {slope_formula}")
print(f" Euclidean Distance: {euclidean_distance}")
print()

# Task 10,compare slope in task8 and 9
slope_comparison = slope == slope_formula
print(f"Comparison of slopes: {slope_comparison}")
print()

# Task 11
# x values
x_values = [-3, -2, -1, 0, 1, 2, 3]

# y_values
y_values = [x**2 + 6*x + 9 for x in x_values]

# find x values where y is 0
zero_y_values= [x for y in zip(x_values, y_values) if y == 0]

# get result
print("Values of x where y is 0:", zero_y_values)
print("Values of y for different x:", y_values)
print()

# Task 12, find length of both words and make falsy comparison
# find the length og python
length_python = len('python')

# find the length of dragon
length_dragon = len('dragon')

# falsy comparison
falsy_comparison = length_python == length_dragon

# printing result
print(f"length of python: {length_python}")
print(f"length of dragon: {length_dragon}")
print(f"Falsy comparison: {falsy_comparison}")
print()

# Task 13, use operator to check if on is found in both python and dragon
on_check = 'on' in 'python' and 'on' in 'dragon'
print(f"'on' found in both 'python' and 'dragon': {on_check}")
print()

# Task 14, check in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
result = "jargon" in sentence
print(result)
print()

# Task 15, check if there is no on  in both python and dragon 

word_1 = "python"

word_2 = "dragon"

result = "on" not in word_1 and "on" not in word_2
print (result)
print()

# Task 16
text = "python"
# find the length of the text
length = len (text)
# convert the length to float
len_float = float(length)
# convert the float to string
len_string =str(len_float)

print("Length as float:", len_float) 
print("Length as string:", len_string)
print()

# Task 17 check even number are divisible by 2 and the remainder is zero
num = 6
if num % 2 ==0:
    print(num, "is even.")
else:
    print (num, "is odd.")
print()

# Task 18
floor_division_check = 7 // 3 == int(2.7)
print(f"Floor division check: {floor_division_check}")
print()

# Task 19
type_check = type('10') == type(10)
print(f"Type check: {type_check}")
print()

# Task 20
result = int(float('9.8') == 10)
print(f"Conversion check: {result}")
print()

# Task 21
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
print()

# calculate pay
pay= hours * rate_per_hour
# result
print(f"the pay is {pay}")
print()

# Task 22
years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds")
print()

# Task 23
for i in range(1, 6):
    print(f"{i} 1 {i} {i*i} {i*i*i}")
