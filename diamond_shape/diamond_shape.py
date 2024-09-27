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
# Print the bottom half of the diamond
    for i in range(n // 2 - 1, -1, -1):
        spaces = ' ' * (n // 2 - i)
        asterisk = '*' * (2 * i + 1)
        print (spaces + asterisk)
# Ask the user for input
width = input("Please enter an odd integer: ")
# Store and convert width into integer in variable n
n = int(width)
# Call the function and check for the return value 
message = print_diamond(n)
# Print the return value only if it's not none
if message != None: 
    print (message)

# End of program