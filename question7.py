# grading system to students

# Get marks from user
marks = float(input("Enter student marks (0 - 100): "))

# Validate marks
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
else:
    # Determine grade
    if marks > 79:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "E"

    print("The grade is:", grade)
