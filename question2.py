
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
number=int(input("Enter a number: "))
if number % 2==0:
    print("number is even")
elif number % 2!=0:
    print("number is odd")
