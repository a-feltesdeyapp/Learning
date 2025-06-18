# Lesson 3: Programming with Data

# Initialize some variables
name = "Beetlebug"
age = 21
heightInInches = 70.5

# Print the variables
# print(name + "'s age is" + age)
    # Reminder that you can't concatenate strings and integers directly in Python.
# Since we're in Python3, you should use f-strings for better readability
print(f"{name}'s age is {age} and height is {heightInInches//12} ft and {heightInInches % 12} in.")