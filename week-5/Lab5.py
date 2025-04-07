"""
Aaron Eberly
Feb 14, 2025
Demonstrate my knowledge of nested for loops
"""

def main():
    option = 0
    while(option != 5):
        # seperate print lines used to make it more readable
        print("========================================")
        print("1. Display and add natural numbers from N to 1")
        print("2. The multiplcation table of N")
        print("3. The pyramid of stars")
        print("4. The pyramid of numbers")
        print("5. Exit")
        print("========================================")
        option = (int)(input("Choose a number: "))
        if(option == 1):
            # Print numbers and add them together
            # Since this number is referred to as N for the user, I decided to keep the variable name as N
            # Even though it's not especially descriptive, it will help avoid confusion
            N = (int)(input("Enter a natural number for N."))
            numberSum = 0
            print(f"Displaying numbers from {N} to 1.")
            for num in range(N, 0, -1):
                # num decreases by 1 every loop
                print(num)
                numberSum += num
            print(f"The sum of all natural numbers from {N} to 1 is {numberSum}")

        elif(option == 2):
            # displays multiplcation tables
            factor1 = (int)(input("Enter a natural number for N: "))
            print(f"Multiplcation table for {N}.")
            for factor2 in range(1, 11):
                # Factor2 will count up from 1 to 10
                print(f"{factor1} x {factor2} = {factor1 * factor2}")

        elif(option == 3):
            # creates a pyramid of stars
            numRows = (int)(input("How many rows of * should there be?"))
            print(f"Creating a star pyramid with {numRows} rows.")
            for row in range(numRows):
                # add 1 to row so that it starts at 1
                row += 1
                for star in range(row):
                    print("*", end = " ")
                print("")
        elif(option == 4):
            # creates an inverse pyramid of numbers
            numberRows = (int)(input("Enter the number of rows for the number pyramid: "))
            print(f"Printing a number pyramid with {numberRows} rows")
            for currentRow in range(numberRows, 0, -1):
                for number in range(currentRow):
                    # space included after each number
                    print(f"{number + 1}", end = " ")
                # print line so that the pyramid moves to the next line
                print("")
        elif(option == 5):
            # Causes the loop to end
            print("Goodbye!")
        else:
            # Only if the user chooses an invalid option
            print("Please enter a number between 1 and 5.")

main()