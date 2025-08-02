# Task 2: Personalized Greeting

# Taking user's name as input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Concatenating full name
full_name = first_name + " " + last_name

# Displaying personalized greeting
print(f"\nHello, {full_name}! Welcome to Python programming!")
