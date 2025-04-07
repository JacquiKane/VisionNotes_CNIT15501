"""
Aaron Eberly
Feb 7, 2025
Demonstrate my knowledge of if and while loops
"""

def main():
    # This variable will track the option that the user has chosen
    option = 0
    while (option != 6):
        #Displayed on different print lines so that it is easier to see while coding
        print("\t\tWhile Loops Lab")
        print("===============================================================")
        print("1. Print all natural numbers between 1 and N")
        print("2. Add ip all natural numbers between 1 and N")
        print("3. Add up all even numbers between 1 and N")
        print("4. Compute the sum of all square numbers between 1 and N")
        print("5. Compute the sum and average of the cube numbers between 1 and N")
        print("6. Exit")
        print("===============================================================")
        # prompt the user for the option they wish to do
        option = (int)(input("Choose one of the above options: "))

        if(option == 1):
            N = (int)(input("Choose a natural number for N: "))
            print(f"Displaying natural numbers from 1 to {3}")
            currentNum = 1
            while(currentNum <= N):
                print(currentNum)
                # Use an augmented operator to increment so that the loop doesn't repeat indefinitely
                currentNum += 1

        elif(option == 2):
            N = (int)(input("Choose a natural number for N: "))
            print(f"Displaying natural numbers from 1 to {N}")
            currentNum = 1
            numberSum = 0
            while(currentNum <= N):
                print(currentNum)
                # Still print all numbers, but also add them together
                numberSum += currentNum
                currentNum += 1
            print(f"The sum of all numbers from 1 to {N} is {numberSum}")

        elif(option == 3):
            N = (int)(input("Choose a natural number for N: "))
            print(f"Displaying even natural numbers from 1 to {N}")
            currentNum = 1
            numberSum = 0
            while(currentNum <= N):
                # The following if statement makes sure that the number is even using modulus
                if(currentNum % 2 == 0):
                    print(currentNum)
                    numberSum += currentNum
                #Increment outside of the if loop. Even if the number is odd, the program moves on
                currentNum += 1
            print(f"The sum of all even numbers from 1 to {N} is {numberSum}")

        elif(option == 4):
            N = (int)(input("Choose a natural number for N: "))
            print(f"Displaying the squares of all numbers from 1 to {N}")
            currentNum = 1
            numberSum = 0
            while(currentNum <= N):
                # Square the number before displaying it
                squaredNum = currentNum ** 2
                print(squaredNum)
                # add each squared number to the total sum
                numberSum += squaredNum
                currentNum += 1
            print(f"The sum of the squares of all numbers from 1 to {N} is {numberSum}")

        elif(option == 5):
            N = (int)(input("Choose a natural number for N: "))
            print(f"Displaying the cubes of all numbers from 1 to {N}")
            currentNum = 1
            numberSum = 0
            while(currentNum <= N):
                # Cube the number before displaying it
                cubedNum = currentNum ** 3
                print(cubedNum)
                # add each cubed number to the total sum
                numberSum += cubedNum
                currentNum += 1
            print(f"The sum of the squares of all numbers from 1 to {N} is {numberSum}")
            # The average is the total divided by the amount of numbers
            average = numberSum / N
            #Round the average to 2 decimal places
            round(average, 2)
            print(f"The average of these numbers is {average}")

        elif(option == 6):
            print("Goodbye!")
            # Since the option chosen is 6, the loop will now end
        else:
            print("Invalid selection. Please enter a number between 1 and 6.")
            # This is an error for if the user chooses an invalid number

main()