"""
Aaron Eberly
Feb 21
Demonstrate for loops
"""

def main():
    option = 0
    #Will continue until the user chooses to exit (option 5)
    while(option != 5):
        #print is split into multiple lines to increase readability
        print("\tFor Loops Lab")
        print("==============================")
        print("1. A multiplcation table")
        print("2. N for N times with commas")
        print("3. The table of stars")
        print("4. The inverted triangle")
        print("5. Exit")
        print("==============================")
        option = (int)(input("choose an option: "))

        if(option == 1):
            #This will create a multiplcation table
            N = (int)(input("Enter a natural number for N: "))
            #Using N as the variable name because the interface refers to it as such
            print(f"Displaying {N} x {N} of a multiplcation table.")
            for factor1 in range(1, N + 1):
                for factor2 in range(1, N + 1):
                    print(factor1 * factor2, end = " ")
                    #specify the end so that it will all print on the same row
                print("")
                # move to the next row

        elif(option == 2):
            # N for N times with commas
            numRows = (int)(input("Enter the number of rows: "))
            for row in range(1, numRows + 1):
                for num in range(1, row + 1):
                    # starts at 1
                    # add 2 to row because index starts at 0
                    if(num == row):
                        print(row)
                        # don't print a comma if it is the last number
                        # this will also end the row
                    else:
                        print(row, end = ", ")

        elif(option == 3):
            # pyramid of stars
            numRows = (int)(input("Enter the number of rows: "))
            print(f"displaying{numRows} rows of the table of stars.")
            for row in range(numRows):
                space = numRows
                for space in range(numRows - row):
                    print("  ", end = "")
                for star in range(row + 1):
                    print("* ", end = "")
                # Some explanation for this double for loop here:
                # The first one (space) creates the correct number of spaces
                # The second one (star) prints stars for the rest of the row
                # it is range row+1 because index starts at 0
                print("")
                #move onto the next line

        elif(option == 4):
            # Inverted triangle of stars
            numRows = (int)(input("Enter the size of the triangle: "))
            print(f"Displaying {numRows} rows of the triangle of stars:")
            numStars = numRows
            for row in range(numRows):
                for space in range(row):
                    print(" ", end = "")
                    #This for loop creates all the spaces I need before I create stars
                for star in range(2 * numStars - 1):
                    print("*", end = "")
                numStars -= 1
                # This will make the number of stars in each row go down
                print("")
                    
        elif(option == 5):
            print("Goodbye!")
            # Because option is now 5, the loop will end
        else:
            print("Please choose an option from 1 to 5.")

main()