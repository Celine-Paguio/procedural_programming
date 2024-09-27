# This program will calculate the voltage, current or resistance.

# Start of program
# Ask for the user to choose what they would like to calculate 
choice = input("What would you like to calculate? Please enter V for Voltage, C for Current, or R for Resistance): ")
# Remove the spaces and capitalize the input if in lowercase"
choice = choice.strip().upper()
# Calculate voltage
if choice == "V":
# Ask for the appropriate values
    current = float(input("Enter the current in Amperes: "))
    resistance = float(input("Enter the resistance in Ohms: "))
# Computation
    voltage = current * resistance
    print("The voltage is %.2f" %voltage, "volts.")
# Handle cases where division by zero might occur