# import pandas as pd
#
# # Read CSV file into a DataFrame
# df = pd.read_csv("all_olympic_medalists.csv")
#
# # Show first 5 rows
# print(df.head())
#
# # Access a column
# print(df["medal"])
#
# # Group by "Category" and sum values in "Sales" column
# result = df.groupby("country")["medal"].value_counts()
# print(result)
#
# print(result.loc['United States'].sum())

'''As the colonists approach Mars, you need to help them calculate their telemetry data.
 To do this, you are going to write a python program.
  The program should ask the user if they would like to input either "Miles above Mars" or
"Kilometers above Mars".  If they choose "Miles above Mars", the program should then
prompt them to enter the number
of miles.  Then the program should display the number of yards, feet,
and inches that are in that many miles.
If the user chooses "Kilometers above Mars", the program should t
hen prompt them to enter the number of kilometers.
Then the program should display the number of meters, centimeters,
 and millimeters that are in that many kilometers.'''

# Mars altitude unit converter
# print("Choose a unit to input:")
# print("1 - Miles above Mars")
# print("2 - Kilometers above Mars")
#
# choice = input("Enter 1 or 2: ").strip()
#
# if choice == "1":
#     miles = float(input("Enter the number of miles: "))
#     yards = miles * 1760
#     feet = miles * 5280
#     inches = miles * 63360
#     print(f"{miles} miles above Mars is equivalent to:")
#     print(f"{yards:,.2f} yards")
#     print(f"{feet:,.2f} feet")
#     print(f"{inches:,.2f} inches")
#
# elif choice == "2":
#     kilometers = float(input("Enter the number of kilometers: "))
#     meters = kilometers * 1000
#     centimeters = kilometers * 100000
#     millimeters = kilometers * 1_000_000
#     print(f"{kilometers} kilometers above Mars is equivalent to:")
#     print(f"{meters:,.2f} meters")
#     print(f"{centimeters:,.2f} centimeters")
#     print(f"{millimeters:,.2f} millimeters")
#
# else:
#     print("Invalid choice. Please restart and enter 1 or 2.")

"""You find the resource file, and you are somewhat surprised to see that the problem that needs to be solved deals with
food.

Here's some backgroudn information.  Martian colonists have simple joys — and pizza is one of them. Due to supply shortages, thin-atmosphere baking challenges, and incoming new colonists every meal must be optimized.

You have been sent to Mars with three Automatrons that were designed specifically for making pizza.  The problem is
that no one has taken the time to figure out which Automatron is most efficient (produces the most pizza with the least
amount of dough).

The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

As the Chief Engineer, you decide to write a Python Script to figure out which Automatron is most efficient.  Once we avert total disaster and save all 1000 lives on board of the incoming shuttle,
we will want to welcome them with some warm, Martian pizza after all.

Write a Python Script to determine which of these are the best deal.  Use functions to calculate the areas of the pizzas.

Once you have completed this, navigate to root directory to find Problem 3."""

import math

# Function for circle area
def circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius ** 2)

# Function for equilateral triangle area
def equilateral_triangle_area(side):
    return (math.sqrt(3) / 4) * (side ** 2)

# Function for square area
def square_area(side):
    return side ** 2

# Automatron 1: 2 circular pizzas, 15 inch diameter, 20 units dough
auto1_area = 2 * circle_area(15)
auto1_efficiency = auto1_area / 20

# Automatron 2: 1 equilateral triangle pizza, side 20, 20 units dough
auto2_area = equilateral_triangle_area(20)
auto2_efficiency = auto2_area / 20

# Automatron 3: 1 square pizza, side 18, 18 units dough
auto3_area = square_area(18)
auto3_efficiency = auto3_area / 18

# Display results
print(f"Automatron 1 efficiency: {auto1_efficiency:.2f} square inches per dough unit")
print(f"Automatron 2 efficiency: {auto2_efficiency:.2f} square inches per dough unit")
print(f"Automatron 3 efficiency: {auto3_efficiency:.2f} square inches per dough unit")

# Determine the best deal
efficiencies = {
    "Automatron 1": auto1_efficiency,
    "Automatron 2": auto2_efficiency,
    "Automatron 3": auto3_efficiency
}

best = max(efficiencies, key=efficiencies.get)
print(f"\nThe best deal is: {best} with {efficiencies[best]:.2f} sq in per dough unit")

import math

# Your module masses from the problem
masses = [
    74364, 146203, 128470, 91616, 115655, 134147, 53470, 126471, 70040, 88750,
    142353, 143329, 86356, 118399, 97959, 148345, 117705, 87624, 63862, 71962,
    106974, 66255, 119735, 78726, 93698, 148680, 144638, 83341, 149571, 147196,
    54526, 91775, 63153, 143441, 71134, 114131, 120931, 109833, 106073, 64547,
    126938, 52877, 89945, 59466, 79660, 147815, 55381, 100052, 78824, 121844,
    104155, 117313, 69305, 144645, 81350, 123512, 81467, 120836, 118612, 143999,
    90792, 71054, 138942, 56481, 71850, 85266, 77437, 86530, 147311, 133699,
    126684, 58708, 149482, 104101, 67985, 81648, 95290, 77155, 76578, 116025,
    83980, 59517, 62078, 89003, 126205, 122542, 116388, 144040, 102560, 77098,
    127534, 56415, 85703, 85580, 86787, 72029, 82533, 132187, 70849, 98839
]

def fuel_required(mass):
    """Calculate fuel for a given mass."""
    return math.floor(mass / 3) - 2

# Calculate total fuel
total_fuel = sum(fuel_required(m) for m in masses)

print(f"Total fuel required: {total_fuel}")
