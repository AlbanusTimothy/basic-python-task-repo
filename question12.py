# largest number of 4 inputs

# Get four numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# Compare step by step (no loops)
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    largest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    largest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    largest = num3
else:
    largest = num4

# Display result
print("The largest number is:", largest)
