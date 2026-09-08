#==================================================================================
#Program: Hypotenuse Calculator
#Author:  John Owen D. Depidep
#Purpose: This program calculates the hypotenuse of a right triangle.
#===================================================================================
import math

# Ask user for the lengths of the two shorter sides
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

# Use math.pow() to square both side lengths
a_squared = math.pow(side_a, 2)
b_squared = math.pow(side_b, 2)

# Add two squared values together
sum_of_squares = a_squared + b_squared

# math.sqrt() to calculate the hypotenuse
hypotenuse = math.sqrt(sum_of_squares)

# Display hypotenuse rounded to two decimal places
print(f"The hypotenuse is: {hypotenuse:.2f}")