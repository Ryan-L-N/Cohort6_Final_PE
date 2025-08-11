import math
#make a list from the file
with open('AI2C-Prereqs/lesson11/Git Working With Others/MISSION/input.txt', 'r') as file:
    lines_list = [int(line.strip()) for line in file]

def fuel_calc(mass):
    #Fuel = floor(mass / 3) - 2
    return math.floor(mass // 3) - 2
#sum of fuel of all modules in the input file
total_fuel = 0

# Iterate through each mass in the list
for mass in lines_list:
    # Apply fuel_calc() and add the result to the total
    total_fuel += fuel_calc(mass)

print(f"The total fuel required is: {total_fuel}")