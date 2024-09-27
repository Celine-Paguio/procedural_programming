# This program that will ask a user to input a temperature and covert it into Celcius or Fahrenheit

# Start of program
# Ask the user to input a temperature
temp = float(input("Please enter the temperature without the unit: "))
# Ask the user to select the type of convertion
convertion = input("Please select the convertion type.\n(1)Celcius to Fahrenheit \n(2)Fahrenheit to Celcius \n")
# Convert the input
# Celcius to Fahrenheit 
if convertion == "1":
    fahrenheit = (temp * (9/5)) + 32
    print(f"{temp}°C is equal to {fahrenheit}°F.")
# Fahrenheit to Celcius
elif convertion == "2":
    celcius = (temp - 32) * (5/9)
    print(f"{temp}°F is equal to {celcius}°C.")  