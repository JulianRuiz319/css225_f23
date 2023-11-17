#Julian Ruiz
#11/4/23
#m6 p6

import math

user_input = int(input("enter a non-negative integer: "))
factorial = 1
for i in range(1, user_input + 1):
    factorial *= i

math_factorial = math.factorial(user_input)
print(f"the factorial of {user_input} (calculated with a for loop) is: {factorial}")
print(f"The factorial of {user_input} (calculated with math.factorial) is: {math_factorial}")