#!/bin/bash

import numpy as np

mass_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        mass_list.append(int(line))

mass_list = np.array(mass_list)

fuel = np.array((mass_list // 3) - 2)

print(fuel)
