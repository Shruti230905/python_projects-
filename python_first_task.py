# Task 1: Basic Mathematical Operations

# Taking input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handling division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero is not allowed)"

    # Displaying the results
    print(f"\nResults of mathematical operations on {num1} and {num2}:")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
