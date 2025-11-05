# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
#calculating area of a triangle
def find_area(base, height):
    area = 0.5 * base * height
    return area

# Main part
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = find_area(base, height)

print(f"The area of the triangle is: {area:.2f}")
