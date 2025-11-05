# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user
# Function to check if number is even or odd
def check_number(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Main part
number = int(input("Enter a number: "))

result = check_number(number)

print(f"The number {number} is {result}.")
