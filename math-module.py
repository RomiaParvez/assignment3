import math  # Importing the math module

# Taking user input
num = float(input("Enter a number: "))

# Calculating required values using the math module
square_root = math.sqrt(num) if num >= 0 else "Undefined (square root of negative number is not real)"
natural_log = math.log(num) if num > 0 else "Undefined (logarithm of non-positive number is not defined)"
sine_value = math.sin(num)  # Sine function works for all real numbers

# Displaying the results
print(f"Square root of {num}: {square_root}")
print(f"Natural logarithm (ln) of {num}: {natural_log}")
print(f"Sine of {num} (in radians): {sine_value}")
