"""
Aaron Eberly
March 7, 2025
Assignment 8
"""

def main():
    exit = False
    while exit == False:
        # Seperate print lines to improve readability
        print("======== User defined function menu ========")
        print("1. Compute n factorial")
        print("2. Sum of all odd numbers from n1 to n2 (n1 <= n2)")
        print("3. Sum of the inverse of all numbers between n1 and n2 (n1 <= n2)")
        print("4. Find the number of characters")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            n = (int)(input("Please enter a natural number for n: "))
            #Even though n isn't descriptive, I use it because thats how the varoable is referred to by the user
            returnVal = factorial(n)
            print(f"{n}! = {returnVal}")

        elif choice == "2":
            print("2. Sum of all odd numbers from n1 to n2 (n1 <= n2)")
            n1 = (int)(input("Enter a natural number for n1: "))
            n2 = (int)(input("Enter a natural number for n2: "))
            #Assumption that n1 is less than n2
            #Once more, undescriptive names because they are what the user sees
            sumOdds(n1, n2)

        elif choice == "3":
            print("3. Sum of the inverse of all numbers between n1 and n2 (n1 <= n2)")
            n1 = (int)(input("Enter a natural number for n1: "))
            n2 = (int)(input("Enter a natural number for n2: "))
            #Assumption that n1 is less than n2
            #Once more, undescriptive names because they are what the user sees
            sumInverse(n1, n2)

        elif choice == "4":
            # Find the number of times a certain character appears in a string
            print("4. Find the number of characters")
            sentence = input("Please enter the string to work on: ")
            character = input("Please enter the character you wish to count in the above string: ")
            character = character.upper()
            # Make sure that uppercase and lowercase are interchangable
            sumChar = findChar(sentence, character)
            print(f"The character {character} appeared {sumChar} times.")

        elif choice == "5":
            print("Goodbye!")
            exit = True
        else:
            print("Please choose a valid input (1-5)")

def factorial(n):
    if n == 0:
        return 1
        #factorial of 0 is 1
    else:
        total = 1
        # Need to start at 1 so that multiplecation works
        for num in range(n):
            num += 1
            # Add 1 to num so that it starts from 1 instead of 0
            total *= num
        return total
    
def sumOdds(n1, n2):
    #Sum all odd numbers from n1 to n2 inclusive
    sum = 0
    for num in range(n1, n2 + 1):
        # add 1 to n2 to make it inclusive
        if(num % 2 == 1):
            # Check to see that the number is odd
            print(num)
            sum += num
    print(f"The sum of the odd numbers is {sum}")
    # This function is supposed to print instead of return

def sumInverse(n1, n2):
    sum = 0
    for num in range(n1, n2 + 1):
        # add 1 to n2 to make it inclusive
        print(f"1 / {num}")
        inverse = 1 / num
        sum += inverse
    print(round(sum, 2))
    # This function prints instead of returning

def findChar(sentence, character):
    # character is already uppercase
    sumChar = 0
    for letter in sentence:
        if letter.upper() == character:
            sumChar += 1
    return sumChar

main()