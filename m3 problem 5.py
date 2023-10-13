#Julian Ruiz
#10/13/23

# Get user input for miles driven and gallons used
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))

# Calculate MPG
mpg = miles_driven / gallons_used

# Print the result
print("Your car's Miles Per Gallon (MPG) is: {:.2f}".format(mpg))


