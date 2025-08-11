"""
#ask user if they want to input
"Miles above Mars"
or
"Kilometers above Mars"
prompt them to enter the value.
if miles:
display answerw in # of yards, feet, and inches

if kilometers:
display in meters, centimeters, and millimeters for that value.
"""
import os
from time import sleep
def clear_screen():
    print(chr(27) + "[2J")
    sleep(1)



user_input = ""
while user_input.upper() != "Q":
    user_input = input("Make a Selection:\n1) Miles above Mars \n2) Kilometers above Mars\n\nor enter Q to quit\n\n")
    if user_input == "1":
        clear_screen()
        distance = float(input("\nEnter the distance in miles").strip())
        # Conversion constants
        INCHES_PER_FOOT = 12
        FEET_PER_YARD = 3
        INCHES_PER_MILE = 63360
        
        # 1. Start with total inches to maintain precision
        total_inches = round(distance * INCHES_PER_MILE)
        
        # 2. Get feet and leftover inches
        total_feet, inches = divmod(total_inches, INCHES_PER_FOOT)
        
        # 3. Get yards and leftover feet
        yards, feet = divmod(total_feet, FEET_PER_YARD)


        print(f"{yards} yards, {feet} feet, and {inches} inches.")
    elif user_input == "2":
        clear_screen()
        
        METERS_PER_KILOMETERS = 1000
        CENTIMETERS_PER_METER = 100
        MILLIMETERS_PER_CENTIMETER = 10
        MILLIMETERS_PER_KILOMETER = 1000000

        distance = float(input("\nEnter the distance in kilometers\n".strip()))
        total_mm = round(distance * MILLIMETERS_PER_KILOMETER)
        total_cm, mm = divmod(total_mm, MILLIMETERS_PER_CENTIMETER)
        meters, cm = divmod(total_cm, CENTIMETERS_PER_METER)
        print(f"{meters} meters, {cm} centimeters, and {mm} millimeters.")
        
    elif user_input.upper() == "Q":
        clear_screen()
        print("Quitting")

    else:
        clear_screen()
        print("ERROR! INVALID INPUT! Enter 1 or 2")
