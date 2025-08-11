

choice = input('Please choose "Miles above Mars" or "Kilometers above Mars": ')

if choice == 'Miles above Mars':
    miles = int(input('Please input number of miles: '))
    yards = miles * 1760
    feet = yards * 3
    inches = feet * 12
    print(f'yards: {yards}, feet: {feet}, inches: {inches}')

elif choice == 'Kilometers above Mars':
    km = int(input("Please input number of km's: "))
    meters = km * 1000
    centi = meters * 100
    milli = centi * 10
    print(f' meters: {meters}, centimeters: {centi}, millimeters: {milli}')
