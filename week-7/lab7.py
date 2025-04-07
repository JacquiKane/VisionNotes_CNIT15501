"""
Aaron Eberly
Feb 28, 2024
Demonstrate nested loops and recursive functions
"""

num1 = 0
num2 = 1

def drawTree(n):
    starsInRow = n - 1
    # This number will start high, and then be lowered
    # This works because a star will be created per star in range(starsInRow, n)
    spaces = (n - 1) / 2
    spaces = int(spaces)
    # Spaces must be converted to an int because the previous calculation made it a float
    for row in range(n, 0, -2):
        for space in range(spaces):
            print(" ", end = "")
            # End must be set to "" so that it doesn't start a new line
        for star in range(starsInRow, n):
            print("*", end = "")
        print("")
        # Move onto new line
        starsInRow -= 2
        spaces -= 1
        # On each new line, there is one less space, but 2 more stars
        # decrease starsInRow to add more stars

def sumOfCubes(n):
    if n == 1:
        return 1
        # stops the recursion. 1 cubed is still 1.
    else:
        return (n ** 3) + sumOfCubes(n - 1)
    
def fibonnacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n - 1) + fibonnacci(n - 2)
    
def main():
    exit = False
    while exit == False:
        n = (int)(input("How many stars should make up the base of the tree? Enter 0 to exit.\n"))
        # because the user is told the variable name n, I will call it n in the code as well
        if n == 0:
            exit = True
            # This is the only option that will stop the loop
        elif n % 2 == 1:
            drawTree(n)
        elif n % 2 == 0:
            n += 1
            # Add one if n is even, so that the tree always turns out nicely
            drawTree(n)

    exit = False
    while exit == False:
        n = (int)(input("Choose a number n. The cubes of all numbers 1 to n will be summed together. (0 to exit)\n"))
        if n == 0:
            exit = True
        elif n != 0:
            print(f"The sum of all cubes from 1 to {n} is {sumOfCubes(n)}")

    exit = False
    while exit == False:
        n = (int)(input("Please enter a positive integer as a Fibonnacci delimiter. (0 to exit)\n"))
        if n == 0:
            exit = True
        elif n != 0:
            print(f"end value: {fibonnacci(n - 1)}")
            # calculate the end value, as specified in the assignment
            # After doing that, I use a for loop to print all of the numbers in the sequence
            # Seems inconvenient, but this is the way I was instructed to do this
            fibStr = ""
            for num in range(n):
                fibStr += str(fibonnacci(num)) + " "
            print(f"Fibonnacci sequence: {fibStr}")

# Making a menu was not required, so instead each function executes after the previous one finishes


main()