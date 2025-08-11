import math

with open(r'C:\Users\Work45\Downloads\input_file_preclass_final_project.txt', 'r') as file:
    lines = file.readlines()

item_mass_list = []
for line in lines:
    item_mass_list.append(float(line.strip()))

#print(item_mass_list)

fuel_needed_per_item = []
for item in item_mass_list:
    fuel_needed = math.floor((item / 3.0)) - 2.0
    fuel_needed_per_item.append(fuel_needed)

#print(fuel_needed_per_item)

total_fuel = sum(fuel_needed_per_item)
print("The total fuel needed is " + str(total_fuel))