"""
Aaron Eberly
April 22, 2025
Review course concepts
"""

global ratingList
ratingList = []
# This list will be used in multiple functions

def rateCourse(courseName):
    print(f"From 1-100, how would you rate {courseName}?")
    # The next question will vary based on the answer
    rating = (int)(input(""))
    ratingList.append(rating)
    # ratingList will be used to find the average rating later
    if rating > 90:
        askQuestion("Why do you like the class so much?")
    elif rating > 60:
        askQuestion("What could make the course more interesting for you?")
    else:
        askQuestion("What aspects of the class fall short? What can we do to improve them?")

def askQuestion(question):
    # Ask the question in the parameter, and append the answer to evaluation.txt
    eval = open("evaluation.txt", "a")
    print(question)
    answer = input("")
    eval.write(f"{answer}\n")
    eval.close()
    # Always good to close files as soon as you are done with them

def main():
    stop = False
    studentNames = ()
    # This list will store every rating entered
    while(stop == False):
        try:
            option = (int)(input("Choose an option:\n1. Evaluate a course\n2. View last evaluation\n3. View average rating\n4. View students\n5. Quit\n"))
            if option < 1 or option > 5:
                raise ValueError
                # Error is an invalid number is chosen
        except ValueError:
            print("Please enter a number 1-5.")
        if option == 1:
            eval = open("evaluation.txt", "w")
            # Because we are opening the file to write, we will overwrite the previous evaluation
            name = input("What is your name?\n")
            studentNames = studentNames + (name,)
            # Must create a new tuple since tuples are immuntable
            courseName = input("What course would you like to evaluate?\n")
            eval.write(f"{name}\n{courseName}\n")
            eval.close()
            rateCourse(courseName)
            askQuestion("How do you like the pace of the course? What can we do to improve the pace of the course?")
            askQuestion("How interesting is the course? What can we do to make you more likely to come to class?")
            askQuestion("Do you feel like the assignments deepen your understanding of the material? How can this be improved?")
            print("Thank you for responding!\n")
            
        elif option == 2:
            # Read the last evaluation by reading the contents of evaluation.txt
            eval = open("evaluation.txt", "r")
            for line in eval:
                print(line)

        elif option == 3:
            # Calculate the average course rating
            total = 0
            for rating in ratingList:
                total += rating
            average = total / len(ratingList)
            # Average automatically becomes a float because python is strongly typed
            print(f"The average course rating is {average}")

        elif option == 4:
            print(f"Students who have responded:")
            for student in studentNames:
                print(student)

        elif option == 5:
            # Quit the program
            print("Thank you")
            stop = True

main()