"""
Aaron Eberly
Feb 13 2025
Demonstrate nested loops
"""

# This part of the code uses nested for loops to print all times tables from 1 to 12

for firstFactor in range(1, 13):
    for secondFactor in range(1, 13):
        print(f"{firstFactor} X {secondFactor} = {firstFactor * secondFactor}")

# This part of the code does the same thing as the first part, but it uses a while loop instead.
# Notice how the while loop takes more lines in this situation.
# While loops and for loops are better at different things.

firstFactor = 1
while(firstFactor <= 12):
    secondFactor = 1
    while(secondFactor <= 12):
        print(f"{firstFactor} X {secondFactor} = {firstFactor * secondFactor}")
        secondFactor += 1
    firstFactor += 1