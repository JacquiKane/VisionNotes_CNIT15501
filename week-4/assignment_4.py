"""
Aaron Eberly
Feb 7, 2025
Demonstrate my knowledge of if statements and math operators
"""
import math

def main():
    programContinue = True
    #Because there is not supposed to be a way to exit the while loop, programContinue is always True
    while(programContinue == True):
        print("\tArea and Volume Calculators")
        print("=====================================")
        print("A. Area of a rectangle")
        print("B. Area of a trapezoid")
        print("C. Volume of a sphere")
        print("D. Volume of a hexagonal pyramid")
        print("E. Volume of an octagonal prism")
        print("=====================================")
        option = input("Choose one of the above options (use capital letters): ")
        if(option == "A"):
            print("Option A: Area of a rectangle")
            #Area of a rectangle. A = wl
            length = (float)(input("Enter the length of the rectangle: "))
            width = (float)(input("Enter the width of the rectangle: "))
            area = length * width
            #Round to 2 decimal places in the f-string
            print(f"The area of the rectangle is {round(area, 2)}")

        elif(option == "B"):
            print("Option B: Area of a trapezoid")
            #Area of a trapezoid
            shortBase = (float)(input("Enter the short base of the trapezoid: "))
            longBase = (float)(input("Enter the long base of the trapezoid: "))
            height = (float)(input("Enter the height of the trapezoid: "))
            area = (shortBase + longBase) / 2 * height
            print(f"The area of the trapezoid is {round(area, 2)}")

        elif(option == "C"):
            print("Option C: Volume of a sphere")
            #volume of a sphere
            radius = (float)(input("Enter the radius of the sphere: "))
            #math.pi will return the value for pi
            volume = (4/3) * math.pi * radius ** 3
            print(f"The volume of the sphere is {round(volume, 2)}")

        elif(option == "D"):
            print("Option D: Volume of a hexagonal pyramid")
            #Volume of a hexagonal pyramid
            baseEdge = (float)(input("Enter the base edge of the hexagonal pyramid: "))
            height = (float)(input("Enter the height of the hexagonal pyramid: "))
            #math.sqrt(x) will take the square root of x
            #PEMDAS is very important to remember here
            volume = (math.sqrt(3) / 2) * baseEdge ** 2 * height
            print(f"The volume of the hexagonal pyramid is {round(volume, 2)}")

        elif(option == "E"):
            print("option E: Volume of an octagonal prism")
            #Volume of an octogonal prism
            baseEdge = (float)(input("Enter the base edge of the octagonal prism: "))
            height = (float)(input("Enter the height of the octagonal prism: "))
            #because of PEMDAS, the baseEdge will be squared before being multiplied
            volume = 2 * (1 + math.sqrt(2)) * baseEdge ** 2 * height
            print(f"The volume of the octagonal prism is {round(volume, 2)}")

        else:
            print("Invalid input. Please enter a letter from A to E.")

main()