# Lesson 4: Distance between Two Points

# Import the math module for mathematical operations
import math

# Initialize some variables
x1, y1 = 1, 2 # Coordinates of the first point
    # Unlike in Matlab, you can assign multiple variables in one line without ;
x2, y2 = 4, 6 # Coordinates of the second point

# Calculate the distance between the two points using the distance formula
A = x2-x1
B = y2-y1
C2 = (A * A) + (B * B)
print(C2) # We still need to take the square root to get the distance
C = math.sqrt(C2)
print(f"The distance between (x: {x1}, y: {y1}) and (x: {x2}, y: {y2}) is {C}")

# If we wanted to let the user input the coordinates, we could do it like this:
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
# Recalculate the distance with user input
A,B = x2-x1, y2-y1
C = math.sqrt((A * A) + (B * B))
print(f"The distance between (x: {x1}, y: {y1}) and (x: {x2}, y: {y2}) is {C}")
