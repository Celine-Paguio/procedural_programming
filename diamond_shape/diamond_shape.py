# This program will create Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.

# Start of program
# Write the print_diamond function
def print_diamond(n):
# Check if the input is an even integer
    if n % 2 == 0:
        return "Please provide an odd integer."
# Print the top half of the diamond
    for i in range(n // 2 + 1):
        spaces = ' ' * (n // 2 - i)
        asterisk = '*' * (2 * i + 1)
        print (spaces + asterisk)
# Ask the user for input
# Call the function
