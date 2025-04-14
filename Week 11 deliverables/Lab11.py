"""
Aaron Eberly
April 4, 2025
Demonstrate lists and exceptions
"""

def stepsToMiles(stepsList):
    miles_walked = []
    # Create an empty list that will eventually be returned
    for steps in stepsList:
        miles = steps / 2000
        # This is the calculation of how many steps go into a mile
        miles_walked.append(round(miles, 2))
    return miles_walked
    # This list will contain the miles conversion from the steps list

def main():
    stepsList = []
    day = 1
    while day <= 7:
        steps = input(f"Enter the number of steps for day {day}: ")
        try:
            steps = int(steps)
            # Cause an error if anything other than numbers are entered
            if steps < 0:
                raise ValueError
                # Cause an error if steps is lower than 0
            stepsList.append(steps)
            day += 1
            # Day is only incremented if the value is valid
        except ValueError:
            print("\nInvalid value entered\nPlease enter an integer value in the correct format.\n")
            # This will not increment day and will prompt the user to try again.

    miles_walked = stepsToMiles(stepsList)
    # Convert the list of steps into a list of miles
    total = 0
    # Each element in miles_walked will add to this. It will be used to compute average
    day = 1
    for miles in miles_walked:
        # The goal of this loop is to nicely print out all the miles
        print(f"Day {day}: {miles} miles")
        total += miles
        day += 1
    average = total / 7
    print(f"\nThe average of miles walked: {round(average, 2)}")

main()