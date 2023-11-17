#Julian Ruiz
#10/27/23



for number in range(1, 51):
    if number % 3==0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print( number)

