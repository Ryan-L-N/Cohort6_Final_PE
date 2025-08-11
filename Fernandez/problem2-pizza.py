import math

"""
The first automaton produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
The second automaton makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
The third automaton creates a square pizza with side length 18, that only requires 18 units of dough.

As the Chief Engineer, you decide to write a Python Script to figure out which automaton is most efficient.  Once we avert total disaster and save all 1000 lives on board of the incoming shuttle,
we will want to welcome them with some warm, Martian pizza after all.
"""
def circle_pizza_area(diameter):
    """Calculates the area of a single circular pizza."""
    radius = diameter / 2
    return math.pi * radius**2

def triangle_pizza_area(side_length):
    """Calculates the area of an equilateral triangle pizza."""
    return (math.sqrt(3) / 4) * side_length**2

def square_pizza_area(side_length):
    """Calculates the area of a square pizza."""
    return side_length**2


"""
Calculates and compares the efficiency of each automaton
to determine the best deal for making pizza on Mars.
"""
print("Mars Pizza Mission: Efficiency Report")
print("---------------------------------------")

# automaton 1: Two Circular Pizzas
auto1_dough = 20
auto1_area = 2 * circle_pizza_area(diameter=15)
auto1_efficiency = auto1_area / auto1_dough
print(f"automaton 1 (Circles) Efficiency: {auto1_efficiency:.2f} sq. in/dough unit")

# automaton 2: One Equilateral Triangle Pizza
auto2_dough = 20
auto2_area = triangle_pizza_area(side_length=20)
auto2_efficiency = auto2_area / auto2_dough
print(f"automaton 2 (Triangle) Efficiency: {auto2_efficiency:.2f} sq. in/dough unit")

# automaton 3: One Square Pizza
auto3_dough = 18
auto3_area = square_pizza_area(side_length=18)
auto3_efficiency = auto3_area / auto3_dough
print(f"automaton 3 (Square)  Efficiency: {auto3_efficiency:.2f} sq. in/dough unit")

print("---------------------------------------")

# Determine the most efficient automaton
efficiencies = {
    "automaton 1 (Circles)": auto1_efficiency,
    "automaton 2 (Triangle)": auto2_efficiency,
    "automaton 3 (Square)": auto3_efficiency
}

best_deal = max(efficiencies, key=efficiencies.get)

print(f"The most efficient choice is the {best_deal}.")


#