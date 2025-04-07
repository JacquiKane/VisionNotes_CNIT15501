"""
Aaron Eberly
March 7, 2025
Lab 8
Demonstrate lists
"""

def printStudents(studentNames, studentGPAs):
    print("================LIST================")
    print("\tName\t\tGPA")
    print("\t_____\t\t_____")
    # Putting the print statements on sperate lines to improve readability
    for student in range(len(studentNames)):
        print(f"\t{studentNames[student]}\t\t{studentGPAs[student]}")

def averageGPA(studentGPAs):
    # compute average by totalling all values and dividing by the length of the list
    total = 0
    for gpa in range(len(studentGPAs)):
        total += studentGPAs[gpa]
    average = total / len(studentGPAs)
    return average, total

def minmax(studentGPAs):
    minimum = min(studentGPAs)
    maximum = max(studentGPAs)
    # min and max are built in python functions
    return minimum, maximum
    # This function returns two seperate values at once

def main():
    studentNames = []
    studentGPAs = []
    # THese will be parallel lists
    numStudents = (int)(input("How many students are in the class? "))
    for student in range(numStudents):
        #This will aska  number of times equal to the number of students
        name = input(f"Enter the name of student #{student  + 1}: ")
        # Add one so that it doesn't start listing from 0
        valid = False
        #If the GPA is not valid, this loop will repeat
        while valid == False:
            gpa = (float)(input(f"Enter the GPA of student #{student + 1}: "))
            if gpa >= 0 and gpa <= 4:
                # Check that the GPA is between 1 and 4
                valid = True
            else:
                print("Please enter a value between 0 and 4 (inclusive)")
        studentNames.append(name)
        studentGPAs.append(gpa)
    printStudents(studentNames, studentGPAs)
    print("===================================")
    average, total = averageGPA(studentGPAs)
    print(f"The average student GPA is: {round(average, 2)}")
    print(f"The sum of the GPAs is: {total}")
    minimum, maximum = minmax(studentGPAs)
    # Returns two seperate values at once
    print(f"The minimum GPA entered is: {round(minimum, 2)}")
    print(f"The maximum GPA entered is: {round(maximum, 2)}")
    # Use round to make sure there are only two decimal places

main()