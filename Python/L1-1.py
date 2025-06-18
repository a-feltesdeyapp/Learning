## Lesson 1: Printing and flow
# Programs are executed from top to bottom
print("My name is Alia")
print("") # This prints a blank line

print('testing')
temp = 'testing'; temp2 = "Testing"
print(type(temp))  # This will return the type of the variable temp
print(type(temp2))
    # There are two types of strings in Python: single quotes and double quotes
    # Both are the same, but you can use one inside the other without escaping
    # This is different from Matlab, where you can only use single quotes
# You can also use triple quotes for multi-line strings

print('''Testing out a multi-line string.
    Here we see the second line.
This would be useful for writing haikus.''')
# Something to note is that Python takes into account the indentation of the code
# particularly when printing multi-line strings
# This is different from Matlab, where you can use semicolons to separate lines
# However, you can also use \n to create new lines in a string, just like in Matlab
print('\nNew Line\n') # I don't know what was going on there for a sec, the terminal wasn't agreeing with my code. it's fixed now though.

# We can run the program by typing python3 hello.py in the terminal
# We can also run the program by pressing F5 in VSCode.
# Pressing F5 technically runs the program in debug mode, which allows us to step through the code line by line.

# Remember that you don't need to use semicolons at the end of each line in Python, unlike Matlab.
# However, you can use semicolons to separate multiple statements on the same line, but this is not recommended.
# It's better to write each statement on a new line for readability.
# You can also use the print() function to print multiple values on the same line, separated by commas.
print("Hello", "World", "from", "Python")  # This will print Hello World from Python on the same line
        # # You can also use the end parameter of the print() function to change the end character.
        # print("Hello", end=" ")  # This will print Hello without a new line at the end
        # print("World", end="!")  # This will print World! on the same line
