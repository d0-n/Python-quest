# Define addition function
def add(a, b):
    return a + b

# Define subtraction function
def subtract(a, b):
    return a - b

# Define multiplication function
def multiply(a, b):
    return a * b

# Define division function
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


# Ask user for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for operation
operation = input("Choose operation (add, subtract, multiply, divide): ")

# Decide which function to call
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation."

# Print result
print(f"Result: {result}")