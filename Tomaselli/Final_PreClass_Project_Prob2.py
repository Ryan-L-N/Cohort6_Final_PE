'''
The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.
'''

import math

pi_value = math.pi

def first_auto() -> str:
    first_auto_total_area = 2*(pi_value*15)
    first_auto_per_unit_dough = first_auto_total_area / 20
    print("The first automatron requires " + str(first_auto_per_unit_dough) + " per unit of dough.")
    return first_auto_per_unit_dough
    
def second_auto() -> str:
    second_auto_total_area = pi_value*(20**2)
    second_auto_per_unit_dough = second_auto_total_area / 20  
    print("The second automatron requires " + str(second_auto_per_unit_dough) + " per unit of dough.")
    return second_auto_per_unit_dough
    
def third_auto() -> str:
    third_auto_total_area = 18**2
    third_auto_per_unit_dough = third_auto_total_area / 18
    print("The third automatron requires " + str(third_auto_per_unit_dough) + " per unit of dough.")
    return third_auto_per_unit_dough

def winner(*args) -> str:
    auto_list = []
    for item in args:
        auto_list.append(item)
    winning_auto = max(auto_list)
    winning_position = auto_list.index(max(auto_list)) + 1
    print("The winning_automatron is at position " + str(winning_position))

def main():
    print("Welcome")   
    first_auto_per_unit_dough = first_auto()
    second_auto_per_unit_dough = second_auto()
    third_auto_per_unit_dough = third_auto()
    winner(first_auto_per_unit_dough, second_auto_per_unit_dough, third_auto_per_unit_dough)
    
if __name__ == "__main__":
    main()
