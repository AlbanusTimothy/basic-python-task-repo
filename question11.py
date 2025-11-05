# writing age of a user

from datetime import date

# Get date of birth from user
year = int(input("Enter birth year (e.g. 2003): "))
month = int(input("Enter birth month (1-12): "))
day = int(input("Enter birth day (1-31): "))

# Create date objects
dob = date(year, month, day)
today = date.today()

# Calculate the difference in days
age_days = (today - dob).days

# Convert to years, months, days
years = age_days // 365
months = (age_days % 365) // 30
days = (age_days % 365) % 30

# Display result
print(f"Your age is {years} years, {months} months, and {days} days.")
