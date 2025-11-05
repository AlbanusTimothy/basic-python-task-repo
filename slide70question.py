# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

# calculating total marks
def calculate_total(maths, eng, swa, sci, sos):
    total = maths + eng + swa + sci + sos
    return total

#calculating average marks
def calculate_average(total):
    average = total / 5
    return average

#determining grade
def find_grade(average):
    if average > 79:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "E"

# Main program
maths = float(input("Enter Maths marks: "))
eng = float(input("Enter English marks: "))
swa = float(input("Enter Kiswahili marks: "))
sci = float(input("Enter Science marks: "))
sos = float(input("Enter Social Studies marks: "))

# Calculating total and average
total = calculate_total(maths, eng, swa, sci, sos)
average = calculate_average(total)
grade = find_grade(average)

# Display results
print("\n--- RESULTS ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
