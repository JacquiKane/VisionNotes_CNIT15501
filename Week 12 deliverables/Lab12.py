"""
Aaron Eberly
April 11, 2025
Demonstrate tuples and exceptions
"""

def main():
    # try:
    #     tuple1 = (1,2,3)
    #     list1 = [1,2,3]
    #     # changing the value of the tuple should cause an error because tuples are immutable
    #     # Now that it's two lists, there should be no error
    #     tuple1[0] = 7
    #     list1[0] = 7
    #     print(list1)
    #     print(tuple1)
    # except TypeError:
    #     print("Type error generated")
    # except Exception as e:
    #     # This will not happen, because the previous except statement was carried out instead
    #     # This saves the error message as the variable e
    #     print("error")
    #     print(e)
    #     # Prints the error message

    # ZeroDivisionError
    try:
        num1 = 3
        num2 = 0
        quotient = num1 / num2
    except ZeroDivisionError:
        print("You can't divide by 0!")

    # IndexError
    try:
        my_list = [1, 2, 4, 7, 8]
        print(my_list[8])
    except IndexError:
        print("Invalid index!")

main()