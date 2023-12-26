# this Python program is designed to calculate area of a triangle with given sides from user

# import math function is given to use mathematical operations in our code
import math
# Get input from user for sides of a triangle

side1 = float(input("Enter length of 1st side of a triangle: "))
side2 = float(input("Enter length of 2nd side of a triangle: "))
side3 = float(input("Enter length of 3rd side of a triangle: "))

# Calculate area of a triangle using formula area = √(s(s-a) * (s-b) * (s-c)) where s = (side1 + side2 + side3) / 2

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))
print(f"Area of triangle with given length of sides is: {area}")