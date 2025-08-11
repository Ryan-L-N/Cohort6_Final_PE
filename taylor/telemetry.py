#!/bin/bash

from math import floor

def calc_miles(miles: float) -> tuple:
    yards = floor(miles * 1760)
    feet = floor((miles - (yards / 1760)) * 5280)
    inches = (miles - (yards / 1760) - (feet / 5280)) * 63360
    return(yards, feet, inches)

def calc_metric(kilometers: float) -> tuple:
    meters = floor(kilometers * 1000)
    centimeters = floor((kilometers - (meters /1000)) * 100_000)
    millimeters = (kilometers - (meters / 1000) - (centimeters / 100_000)) * 1_000_000
    return(meters, centimeters, millimeters)

selection = int(input('Choose a standard of measurement:' \
                      '\n[0]Miles Above Mars' \
                      '\n[1]Kilometers Above Mars' \
                      '\nYour Selection: '))

if selection == 0:
    distance = float(input('\nEnter the miles: '))
    measurements = calc_miles(distance)
    print(f'\nYards: {measurements[0]}')
    print(f'Feet: {measurements[1]}')
    print(f'Inches: {measurements[2]}')

else:
    distance = float(input('\nEnter the kilometers: '))
    measurements = calc_metric(distance)
    print(f'\nmeters: {measurements[0]}')
    print(f'centimeters: {measurements[1]}')
    print(f'millimeters: {measurements[2]}') 