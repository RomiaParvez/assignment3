def factorial(n):
    """Calculate factorial using a loop."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i  # Multiply result by current number i
    return result

# Sample input
num = int(input("Enter a number: "))  # Taking user input
print(f"Factorial of {num} is: {factorial(num)}")  # Calling the function and printing result
