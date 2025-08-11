"""Okay, great.  You found the telemetry file.

As the colonists approach Mars, you need to help them calculate their telemetry data.  
To do this, you are going to
write a python program.  
The program should ask the user if they would like to input either "Miles above Mars" or
"Kilometers above Mars". 
 If they choose "Miles above Mars", the program should then prompt them to enter the number
of miles. 
 Then the program should display the number of yards, feet, and inches that are in that many miles.
If the user chooses "Kilometers above Mars", the program should 
then prompt them to enter the number of kilometers.
Then the program should display the number of meters, centimeters, 
and millimeters that are in that many kilometers.

Once you solve this problem, proceed to find the resource file in the file system."""
import math

measurement_choice=input("Would you like to calculate in Kilometers or Miles: ")


def Miles_above_Mars():
    miles_to_yards=1760
    yards_to_feet=3
    feet_to_inches=12
    
    miles= input("Enter miles: ")
    miles = float(miles)
    yards= miles * miles_to_yards
    feet= yards * yards_to_feet
    inches= feet *feet_to_inches

    print (f"{miles} miles is equal to:")
    print(f"{yards:.2f} yards")
    print(f"{feet:.2f} feet")
    print(f"{inches:.2f} inches")


def Kilometers_above_Mars():
    kilos_to_meters= 0.1
    meters_to_centimeters= 0.1
    centimeters_to_millimeters= 0.1
    kilometers = input("Enter kilometers: ")
    kilometers = float(kilometers)

    meters= kilometers * kilos_to_meters
    centimeters= meters * meters_to_centimeters
    millimeters= centimeters * centimeters
    print (f"{kilometers} kilometers is equal to: ")
    print(f"{meters:.2f} meters")
    print (f"{centimeters:.2f} centimeters")
    print (f"{millimeters:.2f} millimeters")

if measurement_choice.lower() == "kilometers":
    Kilometers_above_Mars()

elif measurement_choice.lower() == "miles":
    Miles_above_Mars()


