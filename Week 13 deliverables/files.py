"""
Aaron Eberly
April 15, 2025
Demonstrate files
"""

# Open a file for writing
fh = open("remind.txt", "w")
fh.write("Exam day is Monday May 5")
fh.write("\nBe in IO240 at...")
fh.close()

# Add more to the file by appending
# fh = open("remind.txt", "w")
# If we open it for writing, it will erase what is already on the file
fh = open("remind.txt", "a")
fh.write(" 10:30 AM sharp")
fh.write("\nBe there or be square!")
fh.close()

# Read from an existing file
fh = open("remind.txt", "r")
# use a for loop
for line in fh:
    print(line)
fh.close()

fh = open("remind.txt")
# default is read
line = fh.readline()
while (line != ""): # EOF condition
    print(line)
    line = fh.readline()
fh.close()

# Put file lines into a list
fh = open("remind.txt", "r")
allTheLines = fh.readlines()
print(allTheLines)
fh.close()

# Flexible method read
fh = open("remind.txt")
fullFile = fh.read()
print("The Full File!!!", fullFile)
fh.close()

# Get certain number of bytes from the file
fh = open("remind.txt")
partialFile = fh.read(40)
print("The Full File!!!", partialFile)
fh.close()

# Use  seek method to advance the file pointer
fh = open("remind.txt")
fh.seek(40)
restOfFile = fh.read()
print("File pointer advenced by seek function, now this is the rest of the file: ", restOfFile)
fh.close()

# Flexible method read
fh = open("remind.txt")
fullFile = fh.read()
print("The Full File!!!", fullFile)
fh.close()