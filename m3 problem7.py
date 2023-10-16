#Julian Ruiz
#10/15/23


def find_return_day(starting_day, length_of_stay):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Calculate the total number of days away
    total_days_away = starting_day + length_of_stay

    # Calculate the return day by taking the modulus of total days away with 7
    return_day_number = total_days_away % 7

    return days_of_week[return_day_number]

# Input from the user
starting_day = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))
length_of_stay = int(input("Enter the length of your stay in nights: "))

# Get the return day
return_day = find_return_day(starting_day, length_of_stay)

# Output the result
print(f"You will return on a {return_day}.")