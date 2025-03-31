"""
Aaron Eberly
Feb 4, 2025
Demonstrate boolean operations
"""

def main():

    print("AND truth tables")
    #True True
    in_1 = True
    in_2 = True
    result = in_1 and in_2
    print(f"{in_1}\tand\t{in_2}\t{result}")

    #False True
    in_2 = False
    result = in_1 and in_2
    print(f"{in_1}\tand\t{in_2}\t{result}")

    #False False
    in_1 = False
    result = in_1 and in_2
    print(f"{in_1}\tand\t{in_2}\t{result}")

    print("OR truth table")
    #True True
    in_1 = True
    in_2 = True
    result = in_1 or in_2
    print(f"{in_1}\tor\t{in_2}\t{result}")

    #True False
    in_2 = False
    result = in_1 or in_2
    print(f"{in_1}\tor\t{in_2}\t{result}")

    #False False
    in_1 = False
    result = in_1 or in_2
    print(f"{in_1}\tor\t{in_2}\t{result}")

    print("NOT truth table")

main()

