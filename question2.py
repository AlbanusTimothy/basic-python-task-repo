
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# If the number is a multiple of 4, print out “divisible by 4”
number=int(input("Enter a number: "))
if number % 2==0:
    print("number is even")
elif number % 4==0:
    print("number is divisible by 4")
else:
    print("number is odd")    
