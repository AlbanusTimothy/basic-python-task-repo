
# Prompt user for a phone number
phone = input("Enter phone number: ")

# Remove any spaces just in case
phone = phone.strip()

# Check and print formatted number
if phone.startswith("+254"):
    print("Formatted phone number:", phone)
elif phone.startswith("0"):
    print("Formatted phone number: +254" + phone[1:])
elif phone.startswith("254"):
    print("Formatted phone number: +" + phone)
elif phone.startswith("7"):
    print("Formatted phone number: +254" + phone)
elif phone.startswith("1"):
    print("Formatted phone number: +254" + phone)
else:
    print("Invalid phone number format")
