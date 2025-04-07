"""
Aaron Eberly
Feb 14, 2025
Demonstrate my knowledge of nested loops
"""

def main():
    # define the variable that will be used to select an option
    option = ""
    # .upper() will account for users chooseing upper or lowercase letters
    while(option.upper() != "F"):
        # Seperate print lines to improve readability
        print("\t\tWhile Loops Menu")
        print("=====================================================")
        print("A. Sum of odd natural numbers from 1 to N")
        print("B. Sum of squares of odd natural numbers from 1 to N")
        print("C. Sum of cubes of even natural numbers from 1 to N")
        print("D. Find the factorial of N")
        print("E. Find the multiplcation table of N")
        print("F. Exit")
        print("=====================================================")
        #prompt user for their option
        option = input("Choose an option: ")
        if(option.upper() == "A"):
            # add together odd natural numbers
            # Because the letter N is displayed for the user, I kept the variable as N to reduce confusion
            # Not very descriptive, but helps reduce confusion
            N = (int)(input("Choose a number for N: "))
            print(f"Displaying odd natural numbers from 1 to {N}")
            currentNum = 1
            sum = 0
            while(currentNum <= N):
                #Checks that number is odd
                if(currentNum % 2 == 1):
                    print(currentNum)
                    sum += currentNum
                # Increment has to be outside of if
                currentNum += 1
            print(f"The sum of all odd natural numbers from 1 to {N} is {sum}")
        # Important to use elif instead of if
        elif(option.upper() == "B"):
            # I am reusing the variable N since it fulfills a similar purpose for multiple options
            # This works because the variable is redefined every time
            N = (int)(input("Choose a number for N: "))
            print(f"Displaying the squares of odd natural numbers from 1 to {N}")
            currentNum = 1
            sum = 0
            while(currentNum <= N):
                #Checks that number is odd
                if(currentNum % 2 == 1):
                    # I have to be careful not to change currentNum.
                    # Instead I create a square variable
                    square = currentNum ** 2
                    print(square)
                    sum += square
                # Increment has to be outside of if
                currentNum += 1
            print(f"The sum of the squares of all odd natural numbers from 1 to {N} is {sum}")
        elif(option.upper() == "C"):
            N = (int)(input("Choose a number for N: "))
            print(f"Displaying the cubes of even natural numbers from 1 to {N}")
            currentNum = 1
            sum = 0
            while(currentNum <= N):
                #Checks that number is even
                if(currentNum % 2 == 0):
                    # I have to be careful not to change currentNum.
                    # Instead I create a cube variable
                    cube = currentNum ** 3
                    print(cube)
                    sum += cube
                # Increment has to be outside of if
                currentNum += 1
            print(f"The sum of the squares of all odd natural numbers from 1 to {N} is {sum}")
        elif(option.upper() == "D"):
            #Find factorial
            N = (int)(input("Choose a number for N: "))
            currentNum = 1
            factorial = 1
            while(currentNum <= N):
                # Factorial multiplies all numbers from 1 to N
                factorial *= currentNum
                currentNum += 1
            print(f"The factorial of {N} is {factorial}")
        elif(option.upper() == "E"):
            # displays multiplcation tables
            N = (int)(input("Enter a natural number for N: "))
            factor = 1
            print(f"Multiplcation table for {N}.")
            while (factor <= 10):
                print(f"{N} x {factor} = {N * factor}")
                factor += 1
        elif(option.upper() == "F"):
            #Choosing this option breaks the loop
            print("Goodbye!")
        else:
            #Only happens if an invalid letter is entered
            print("Invalid input. Please input a letter from A to F.")

main()