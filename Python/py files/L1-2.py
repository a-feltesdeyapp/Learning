# Lesson 2: Arithmentic and comparing numbers
print("\nComputers are good at math, but they are not good at reading minds.\n")
# print(10+5)
# print(10-7)
# print(3*102)  # Basic math is easy. The issues come in when we start doing division.

print(10/3) # This will return a float
    # Note that in Python 3, division always returns a float, even if the result is a whole number.
    # Also note that there is a 5 at the end of the result. This stops the computer from storing infinite precision.
print(16//8) # This will return an int
print(20%8) # This will return the remainder of the division. Mod operator.
print(2**3) # This will return 8, which is 2 raised to the power of 3
# You can combine float and intergers, but you will get a float as a result

# Python also follows PEMDAS
print(2*(3-5))

# # Comparison operators are the same as in Matlab
# print(10 == 10)  # This will return True
# print(10 != 10)  # This will return False
# print(10 > 5)    # This will return True
# print(10 < 5)    # This will return False
# print(10 >= 10)  # This will return True
# print(10 <= 5)   # This will return False
# # You can also compare strings, but they will be compared lexicographically
# print('a' == 'a')  # This will return True
# print('a' != 'b')  # This will return True
# print('a' > 'b')    # This will return False
# print('a' < 'b')    # This will return True
# print('a' >= 'a')  # This will return True
# print('a' <= 'b')   # This will return True

# You can also compare strings with numbers, but they will be compared lexicographically
    # Why? Because Python treats strings as sequences of characters, and the string '1' is lexicographically less than the integer 1.
print('1' == 1)  # This will return False
print('1' != 1)  # This will return True
# print('1' > 1)    # This should return False but I received an error
    # Note: The comparison of a string with an integer will raise a TypeError in Python 3.
    # However, if you convert the integer to a string, then the comparison will work
# print('1' < 1)    # This will return True
# print('1' >= 1)  # This will return False
# print('1' <= 1)   # This will return True
    # In Python2, comparing a string with an integer would return False, but in Python 3, it raises a TypeError.
    # Generally, just compare like variables.

# Lexicographic comparison is the same as in Matlab
# As a reminder, lexicographic comparison is the comparison of strings based on the order of their characters in the ASCII table.
# For example, 'a' is less than 'b', and 'A' is less than 'a'.
# Characters are compared from L>R and if all characters equal up to the length of the shorter string, the shorter string is considered smaller.
# If you convert integers to strings, then lexicographical order applies:
# "12" > "100" (because '1' == '1', '2' > '0')
# "2" > "10" (because '2' > '1')

# You can also use the in operator to check if a string is in another string
print('')
print("Hello" in "Hello World")  # This will return True

# + can also be used for concatenation of strings
print("Hello" + " " + "World")  # This will return Hello World
# You can also use the * operator to repeat a string
print("Hello " * 3)  # This will return Hello Hello Hello
# However, you cannot combine strings and numbers with the + operator
# Instead, you can convert the number to a string, or use f-strings (equivalent to %n or %2f in Matlab)

print("1+1 = " + str(1 + 1))  # This will return 1+1 = 2
print(f"2+1 = {2+1}")   # However, unlike Matlab, you call the variable within the f-string with curly braces, not after the string.