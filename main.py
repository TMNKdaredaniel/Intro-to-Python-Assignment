# input 2 numbers and a mathematical operator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (addition, subtraction, multiplication, or division): ")

# print the operation from user's input
print(f"\nYour Operation: {num1} {operator} {num2}")

# Perform the calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = "Error: Division by zero!"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operator!"

# Display the result
print(f"The Final Result: {result}")
