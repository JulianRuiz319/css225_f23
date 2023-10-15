#Julian Ruiz
#10/15/23

#convert degrees Fahrenheit to degrees Celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

# Input from the user
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# Call the function to convert Fahrenheit to Celsius
celsius_result = fahrenheit_to_celsius(fahrenheit_input)

# Display the result
print(f"{fahrenheit_input} degrees Fahrenheit is equal to {celsius_result:.2f} degrees Celsius.")