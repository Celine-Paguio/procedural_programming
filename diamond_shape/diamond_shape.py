# This program will create Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.

# Write the print_diamond function
def print_diamond(n):
# Check if the input is an even integer
    if n % 2 == 0:
        return "Please provide an odd integer."
# Ask the user for input
# Call the function