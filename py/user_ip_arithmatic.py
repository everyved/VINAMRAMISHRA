# Accept input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
sum_result = num1 + num2  # Addition
difference = num1 - num2  # Subtraction
product = num1 * num2  # Multiplication

# Check for division by zero
if num2 != 0:
    quotient = num1 / num2  # Division
    remainder = num1 % num2  # Modulus
else:
    quotient = "Undefined (division by zero)"
    remainder = "Undefined (division by zero)"

# Display results
print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
