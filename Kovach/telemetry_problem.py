# telemetry_python_problem1.txt home/Cohort6/Folder1/Folder22/Folder26/telemetry_python_problem1.txt

"""Okay, great.  You found the telemetry file.

As the colonists approach Mars, you need to help them calculate their telemetry data.  To do this, you are going to
write a python program.  The program should ask the user if they would like to input either "Miles above Mars" or
"Kilometers above Mars".  If they choose "Miles above Mars", the program should then prompt them to enter the number
of miles.  Then the program should display the number of yards, feet, and inches that are in that many miles.
If the user chooses "Kilometers above Mars", the program should then prompt them to enter the number of kilometers.
Then the program should display the number of meters, centimeters, and millimeters that are in that many kilometers.
"""

# TO-DO: Remedy the logic error for the returned distances (labeled with "FIX-ME:")

# First, retrieve user input
def get_user_choices():
    while True:
       user_choice = input('Would you like to calculate "Miles above Mars" or "Kilometers above Mars": ')

       if user_choice != 'Miles above Mars' and user_choice != 'Kilometers above Mars':
           print('Please enter either "Miles above Mars" or "Kilometers above Mars"')
           continue

       return user_choice


# Second, retrieve the value of miles or kilometers
def get_user_value():
    while True:
        user_value = input('Please enter the value: ')

        if user_value.isdigit():
            return int(user_value)

        print('Please enter a valid number')

# Third, calculate the total yards, feet, inches for miles
# FIX-ME: yards, feet, and inches should be the total of those values combined to travel that many miles
def calculate_telemetry_std(user_value):
    yards = user_value * 1760
    feet = yards * 12
    inches = feet * 12

    return yards, feet, inches

# Fourth, calculate the meters, centimeters, and millimeters
# FIX-ME: meters, centimeters, and millimeters should be the total of those values combined to travel that many kilometers
def calculate_telemetry_metric(user_value):
    meters = user_value * 1000 # Retrieve the meters
    centimeters = meters * 100
    millimeters = centimeters * 10

    return meters, centimeters, millimeters


def main():
    user_choice = get_user_choices()
    user_value = get_user_value()

    if user_choice == 'Miles above Mars':
        yards, feet, inches = calculate_telemetry_std(user_value)
        print(f'Your value is {yards} yards, {feet} feet, or {inches} inches')

    elif user_choice == 'Kilometers above Mars':
        meters, centimeters, millimeters = calculate_telemetry_metric(user_value)
        print(f'Your value is {meters} meters, {centimeters} centimeters, or {millimeters} millimeters')



main()