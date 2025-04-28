"""
Aaron Eberly
April 25 2025
Demonstrate files and exception handling
"""

def main():
    try:
        books = open("books.txt", "r")
        analyze = open("analyzedBooks.txt", "w")
        # since the file has been opened for writing, it will overwrite anything already on the file
        bookList = books.readlines()
        for book in bookList:
            book = book.rstrip()
            # remove trailing characters
        analyze.write(f"Printing the contents of the file...\n\n{bookList}")
        analyze.write(f"\n\nNumber of books in the file: {len(bookList)}\n\n")
        analyze.write("Titles of books with more than 2 words:\n")
        for book in bookList:
            titleWords = book.split()
            #  This method will split a string with spaces into a list of strings.
            if len(titleWords) > 2:
                analyze.write(book)
                # This will write all of the books with a title that has more than two words
        analyze.write("\n\nOrganized book titles:\n\n")
        for book in bookList:
            titleBook = book.title()
            analyze.write(titleBook)
        books.close()
        analyze.close()
        # Close files after use

    except FileNotFoundError:
        # This exception will be thrown if the file can't be found in the specified location
        print("The program failed to open the file. Make sure of the following:\nThe file to read is located in the same folder ast he program.\nThe file's name is spelled correctly.")



main()