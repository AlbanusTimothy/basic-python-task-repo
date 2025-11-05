# taking email and password credentials

# Correct login credentials
correct_email = "admin@mail.com"
correct_password = "Admin@123"

# Allow 3 tries
for attempt in range(1, 4):
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email == correct_email and password == correct_password:
        print("Login is Successful ✅")
        break
    else:
        print("Invalid username or password ❌")
        print("Attempt", attempt, "of 3")

        if attempt == 3:
            print("You have been blocked 🚫")

