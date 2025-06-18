# REPL: Read Eval Print Loop
# Open in terminal by typing python3
##### Print
# Use print() to print text to the screen. Feed in arguments
print('Hello World')
## Data Types
    ## Basic
        # integers [int] [immutable]
        # floating point numbers
        # complex numbers
        # booleans  [immutable]
        # strings   [immutable]
    ## Advanced
        # Tuples    [immutable]
        # Lists     [think cells] [mutable]
        # Ranges    
        # Dictionaries  [mutable]
        # Sets      [mutable]

##### Working with text
    # Use underscores for variable names (air_rho) but camel-case for class names (gameScoreStorage)
    # Escape quotes the same as done in LaTeX \'
    # """ Allows for multiline strings """, also can be used to use "" and '' within a string w/o needing to escape
    # \n newline, \r carriage return, \t tab character \\ slash char
    # Unix OS naturally implements the carriage return. Windows does not.
    # Press tab twice to get a list of all string operations
        # Common operations:
        # len() : length
        # .split('operator'): splits string by gvn operator, () defaults to whitespace
        # .replace(): can replace letters or entire words
    # Unlike Matlab, counting starts at 0.
    # Can call strings with slicing (like linspace through an array in Matlab [start:end:step])
## Slicing
mystring = 'beetlebug'
print(mystring[::1])    # prints full string
print(mystring[::2])    # prints belbg (skips every other letter)
print(mystring[::-1])   # prints gubelteeb (reverses order)
print(mystring[2::])    # prints from the third letter (order 2)
## Chaining Calls
print('Hello world'.replace('world','student'.upper()))
## f-strings
    # f outside of the string tells it to look for curly braces. Really useful for printing the name and content of a variable quickly.
age = 21
print(f'My age is {age}')

##### Booleans and Loops
## Boolean is the same as a logical more or less. Use with the comparison operators [Note, != is not equal]
    # Capitals are "smaller" than lowercase ['M' < 'm']
    # Numbers are smaller than letters ['1' < 'a']
# Logical operators also exist
    # and, or, not
# Cannot compare int to str. Can compare bool to int
## if else does not need an end in Python
door_is_locked = True
if door_is_locked:
    print("It's locked.")
else:
    print('The door opens.')
door_is_locked = False
if door_is_locked:
    print("It's locked.")
else:
    print('The door opens.')
## for also doesn't require an end. this feels weird to me but whatever.
mylist = [1,'a','Hello']
for item in mylist:
    print(item)
## again, no end for while
    # break out of infinite loops with ^C (ctrl C)
i = 1
while i <= 4:
    print(i)
    i=i+1