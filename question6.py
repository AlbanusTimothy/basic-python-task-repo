# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked

# Set the correct password
correct_password = "admin@123"

# Allow 4 attempts
for attempt in range(1, 5):
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access granted ✅")
        break
    else:
        print("Incorrect password. Attempt", attempt, "of 4")

        # If this was the 4th (last) attempt
        if attempt == 4:
            print("Account blocked 🚫")


