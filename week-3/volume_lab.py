"""
Aaron Eberly
eberly6@purdue.edu
Jan 31, 2025
9:30 lab section
Demonstrate my knowledge of math functions by calculating volume.
"""

def main():
    depth1 = (int)(input("What is the depth of the shallow end of the pool?"))
    depth2 = (int)(input("What is the depth of the deep end of the pool?"))
    width = (int)(input("What is the width of the pool?"))
    length = (int)(input("What is the length of the pool?"))

    #Check to see if the pool dimensions make sense
    if (depth1 > depth2):
        print("Invalid input! The deep end must be deeper than the shallow end of the pool!")

    #If the dimensions are valid, proceed with calculations
    else:
        print("Calculating...")
        #Calculate using the provided equations. remember PEMDAS
        sideArea = ((depth1 + depth2) * length / 2)
        bottomArea = ((((depth2 - depth1) ** 2 + length ** 2) ** 0.5) * width)
        volume = sideArea * width

        #round results
        sideArea = round(sideArea, 2)
        bottomArea = round(bottomArea, 2)
        volume = round(volume, 2)

        #convert results to str

        sideArea = str(sideArea)
        bottomArea = str(bottomArea)
        volume = str(volume)

        #print results
        print("The side area of the pool is " + sideArea)
        print("The bottom area of the pool is " + bottomArea)
        print("The volume of the pool is " + volume)

main()

#This code used 7 variables