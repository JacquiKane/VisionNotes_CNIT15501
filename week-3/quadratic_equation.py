"""
Aaron Eberly
Jan 31, 2025
12:30 section
Demonstrate PEMDAS with the quadratic formula
"""

import math

def main():
    #Prompt user for the three numbers
    a = input("Enter coefficient a ")
    b = input("Enter coefficient b ")
    c = input("Enter coefficient c ")

    print("The quadratic equation is " + a + " * X^2 " + b + " * X " + c + " = 0")

    #Convert the numbers to a float
    a = float(a)
    b = float(b)
    c = float(c)

    # I will do the lowest coefficient calculation now, before I change the coefficient variable types to str
    lowestCoefficient = min(a, b, c)
    lowestCoefficient = str(lowestCoefficient)

    # Calculate and display the discriminant
    D = (b ** 2 - 4 * a * c)
    D = round(D, 2)
    D = str(D)
    print("The discriminant is " + D)
    D = float(D)

    # The discriminant decides if there is 2, 1, or no real roots
    if(D > 0):
        root1 = (((b * -1) + (D ** (1 / 2))) / (2 * a))
        root2 = (((b * -1) - (D ** (1 / 2))) / (2 * a))
        root1 = round(root1, 2)
        root2 = round(root2, 2)
        root1 = str(root1)
        root2 = str(root2)
        print("The equation has two real roots: " + root1 + " and " + root2)
    
    elif(D == 0):
        root1 = ((-1 * b) / (2 * a))
        root1 = round(root1, 2)
        root1 = str(root1)
        print("The equation has one real root: " + root1)

    # This triggers only if D is less than 0
    else:
        print("The equation has no real roots.")

    # The lowestCoefficient variable has already been calculated
    print("The lowest coefficient is " + lowestCoefficient)


main()