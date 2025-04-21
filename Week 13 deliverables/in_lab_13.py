"""
Aaron Eberly
April 18 2025
Demonstrate exception and file handling
"""

def main():
    try:
        inputFile = open("scores.txt", "r")
        # Even if I don't include "r", the file will be in reading mode as a default

        # This block of code creates a list of float scores without the student names
        scoreList = []
        allLines = inputFile.readlines()
        sum = 0
        # We will find the sum now so we don't have to do it later with another loop
        for line in allLines:
            line = line.split(":")
            score = line[1].rstrip()
            score = float(score)
            sum += score
            scoreList.append(score)
        
        inputFile.close()
        # It's a good idea to close the file as soon as you're done with it

        print(f"Printing the contents of the file...\n{scoreList}")
        minimum = min(scoreList)
        maximum = max(scoreList)
        length = len(scoreList)
        average = sum / length

        outputFile = open("scores_stat.txt", "w")
        # The "w" means that the file is in writing mode.
        # All previous data will be overwritten
        outputFile.write(f"Minimum: {minimum}\nMaximum: {maximum}\nLength: {length}\nAverage: {average}")
    except FileNotFoundError:
        print("The program failed to open the file. Make sure the file is located in the same folder as the program, and the file name is spelled correctly.")
        

main()