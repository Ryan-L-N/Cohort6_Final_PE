"""You find the resource file, and you are somewhat surprised to see that the problem that needs to be solved
deals with food.

Here's some background information.  Martian colonists have simple joys — and pizza is one of them. Due to supply
shortages, thin-atmosphere baking challenges, and incoming new colonists every meal must be optimized.

You have been sent to Mars with three Automatrons that were designed specifically for making pizza.  The problem is
that no one has taken the time to figure out which Automatron is most efficient (produces the most pizza with the least
amount of dough).

*** Compare the Automatrons below to solve the problem ***
The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

As the Chief Engineer, you decide to write a Python Script to figure out which Automatron is most efficient.
Once we avert total disaster and save all 1000 lives on board of the incoming shuttle,
we will want to welcome them with some warm, Martian pizza after all.

Write a Python Script to determine which of these are the best deal.  Use functions to calculate the areas of the pizzas.

Once you have completed this, navigate to root directory to find Problem 3.
"""
import automatron

automatron_1 = automatron.Automatron(15, "circle", 15, 2)
automatron_2 = automatron.Automatron(20, "triangle", 20, 1)
automatron_3 = automatron.Automatron(18, "square", 18, 1)

def main():
    print(f'Automatron 1: {automatron_1.calculate_area()} square inches')
    print(f'Automatron 2: {automatron_2.calculate_area()} square inches')
    print(f'Automatron 3: {automatron_3.calculate_area()} square inches')

    print()

    print(f"Automatron 1: {automatron_1.calculate_area_per_unit()} square inches per unit of dough")
    print(f"Automatron 2: {automatron_2.calculate_area_per_unit()} square inches per unit of dough")
    print(f"Automatron 3: {automatron_3.calculate_area_per_unit()} square inches per unit of dough")


main()