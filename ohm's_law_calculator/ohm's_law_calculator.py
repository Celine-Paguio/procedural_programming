# This program will calculate the voltage, current or resistance.

# Start of program
# Ask for the user to choose what they would like to calculate 
choice = input("What would you like to calculate? Please enter V for Voltage, C for Current, or R for Resistance): ")
# Remove the spaces and capitalize the input if in lowercase"
choice = choice.strip().upper()
# Ask for the appropriate values
# Calculate for the missing variable
# Handle cases where division by zero might occur