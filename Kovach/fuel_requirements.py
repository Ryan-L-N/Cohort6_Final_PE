"""Our inbound colonists rapidly approach Mars atmosphere, but we still do not have reliable comms with them.
We must rapidly launch our spare rocket to establish comms and share the correct telemetry data with them
before they smash into Mars!

There's no time to unload the modules that are on the rocket, and we must begin fueling right away.
The problem is, we do not know how much fuel we need.

As you rush to the rocket, you notice a list of all of the modules' mass on board (your python file input).

Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.

As the Chief Engineer, you need to calculate the total fuel requirement.
To find the total fuel requirement, individually calculate the fuel needed for the mass of each module
 (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?"""

with open("fuel_input.txt", "r") as file:
    modules = file.readlines()
    total_fuel = 0
    for module in modules:
        fuel_requirement = int(module) // 3 - 2
        total_fuel += fuel_requirement
    print(f"Total Fuel: {total_fuel} gallons")
