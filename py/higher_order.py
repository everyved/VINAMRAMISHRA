def apply_operation(x, y, operation):
    return operation(x, y)  # Function is passed as an argument

# Defining two functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Using apply_operation with different functions
print(apply_operation(5, 3, add))       # Output: 8
print(apply_operation(5, 3, multiply))  # Output: 15
