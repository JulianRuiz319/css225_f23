#Julian ruiz
#11/4/23
#m6 p4

import math

num_terms = 100000
approximation = 0

for k in range(num_terms):
    approximation += (-1) ** k / (2 * k +1)

approximation *= 4

print("approximation of pi:", approximation)
print("value of pi from math module:", math.pi)


