"""
Aaron Eberly
Feb 21, 2025
"""

import math

def printInfo():
    # This function prints my info.
    # print lines are split up for readability
    print("**********************")
    print("* Aaron Eberly       *")
    print("* eberly6@purdue.edu *")
    print("* CNIT 15501 lab 6   *")
    print("**********************")

def validate(side1, side2, side3):
    #This will validate if a triangle is possible.
    print("\nValidating triangle...\n")
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

def computeArea(side1, side2, side3):
    #This will compute the area of a triangle
    s = (side1 + side2 + side3) / 2
    # Variable name s is used because that is the constant used in the math formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def findMin(side1, side2, side3):
    #Return the smallest of the three sides
    if(side1 <= side2 and side1 <= side3):
        return side1
    elif(side2 <= side1 and side2 <= side3):
        return side2
    elif(side3 <= side1 and side3 <= side2):
        return side3
    # by using less than or equal to, it means that even if the sides are even, the smallest will be returned
    
def findMax(side1, side2, side3):
    #Return the smallest of the three sides
    if(side1 >= side2 and side1 >= side3):
        return side1
    elif(side2 >= side1 and side2 >= side3):
        return side2
    elif(side3 >= side1 and side3 >= side2):
        return side3
        
def main():
    continueProgram = "Y"
    printInfo()
    #display my info only once, at the beginning
    while(continueProgram.upper() != "N"): 
        # Continue program will only turn false when N or n is entered
        side1 = (int)(input("Enter the length of side 1 of the triangle: "))
        side2 = (int)(input("Enter the length of side 2 of the triangle: "))
        side3 = (int)(input("Enter the length of side 3 of the triangle: "))
        validTriangle = validate(side1, side2, side3)
        if(validTriangle):
            print("This is a valid triangle.")
            # calculate the area, min, and max for my upcoming print statements
            area = computeArea(side1, side2, side3)
            minValue = findMin(side1, side2, side3)
            maxValue = findMax(side1, side2, side3)
            # There are keywords for min and max, but I am not supposed to use them here
            print(f"The area of this triangle is {round(area, 2)}.")
            # rounded to 2 decimal places
            print(f"The smallest side is {minValue}, and the largest side is {maxValue}.\n")
            validResponse = False
            while(validResponse == False):
                continueProgram = input("Would you like to continue? (Y/N): ")
                if(continueProgram.upper() == "Y"):
                    # .upper() is used so that it works with upper and lowercase
                    validResponse = True
                elif(continueProgram.upper() == "N"):
                    # Because continueprogram is now N, the loop will stop
                    validResponse = True
                else:
                    print("Invalid Input\nPress Y or N, case-insensitive")
        else:
            print("This is an invalid triangle. Please try again.\n")
            # according to the example, the user is not given an option to quit if they have an invalid triangle
    print("End of program")
main()