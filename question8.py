# speed checker

# Get speed input from user
speed = int(input("Enter the speed of the car (in km/h): "))

# Check speed
speed_limit=70
speed_exceeded=speed-speed_limit
if speed < 70:
    print("Ok ✅")
else:
    # Calculate demerit points
    points = (speed - 70) // 5
    if speed_exceeded%5 !=0:
        points +=1

    print("Points:", points)

    # Check if license should be suspended
    if points > 12:
        print("License suspended 🚫")
