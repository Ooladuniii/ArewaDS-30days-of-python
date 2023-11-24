import numpy as np

def calculate_square_root(number):
    return np.sqrt(number)

# Example usage without input
num_to_cal = float(input("Enter a number to calculate the square root: "))
result = calculate_square_root(num_to_cal)
print(f"The square root of {num_to_cal} is: {result}")

# Example usage with defined number
num_to_cal = 4
result = calculate_square_root(num_to_cal)
print(f"The square root of {num_to_cal} is: {result}")

