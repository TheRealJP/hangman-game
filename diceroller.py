# Simple Dice Rolling Simulator
# By Juan Ortiz

import random

min = 1
max = 12

rollAgain = 'yes'

while rollAgain == 'yes' or rollAgain == 'y':
        print("Rolling dice...")
        print(random.randint(min, max))
        print(random.randint(max, max))
        rollAgain = input("Roll again?")