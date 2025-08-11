"""
The first Automatron produces 2 circular pizzas (15 inch diameter)
 that require 20 units of dough.
The second Automatron makes a larger, equilateral triangle pizza, 
side length 20, that also requires 20 units of dough.
The third Automatron creates a square pizza with side length 18, 
that only requires 18 units of dough.

As the Chief Engineer, you decide to write a Python Script to 
figure out which Automatron is most efficient.  
Write a Python Script to determine which of these are the best deal.
  Use functions to calculate the areas of the pizzas.

Once you have completed this, navigate to root directory to find Problem 3."""
import math

pizza1_measurement= 15
pizza1_price= 20
pizza2_measurement= 20
pizza2_price= 20
pizza3_measurement=18
pizza3_price=18

area_pizza1= math.pi * (pizza1_measurement* .5)**2
area_pizza2= (math.sqrt(3)/4) * (pizza2_measurement **2)
area_pizza3= pizza3_measurement * pizza3_measurement

def pizza_per_price(area, price, quantity):

    return(float((area* quantity)/ price))

pizza1_deal=pizza_per_price(area_pizza1, pizza1_price,2)
pizza2_deal=pizza_per_price(area_pizza2,pizza2_price,1)
pizza3_deal=pizza_per_price(area_pizza3, pizza3_price,1)
my_deals= {"Pizza 1": pizza1_deal, "Pizza 2": pizza2_deal,"Pizza 3": pizza3_deal}
max_key=max(my_deals, key=my_deals.get)
best_deal= (max_key)
print(best_deal)


