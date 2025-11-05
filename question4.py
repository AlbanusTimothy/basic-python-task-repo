# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email

# Get email from user input
email = input("Enter your email: ")

# Validate the email
if "@" in email and "." in email:
    print("Valid email address ✅")
else:
    print("Invalid email address ❌")
