# programme dding two values input by user

while True:
    try:
        # Get first number
        num1 = float(input("Enter first number: "))

        # Get second number
        num2 = float(input("Enter second number: "))

        # Calculate sum
        total = num1 + num2

        # Display result
        print("The sum is:", total)
        break  # Exit loop if inputs are valid

    except ValueError:
        print("Invalid character entered ❌. Please enter numbers only.\n")
