"""
Aaron Eberly
March 28, 2025
Demonstrate functions with lists
"""

def discount(prices):
    update = []
    # Create an empty list which will hold the discounted prices
    for price in prices:
        price *= .7
        # This is the 30% discount required by the assignment
        update.append(price)
    return update
# Returns the new prices as a different list
        
def printInfo(names, IDs, prices):
    # This function nicely lays out the info on each item
    print("\tName\tID\tPrice")
    print("=================================")
    index = 0
    # Lists start at index 0
    for item in names:
        # Any of the lists work for this loop. I just need to make sure there are the right amount of items printed
        print(f"\t{names[index]}\t{IDs[index]}\t{round(prices[index], 2)}")
        # print each value with a tab between them
        index += 1
    print("=================================")

def search(names, IDs, prices):
    index = 0
    # Index used to match corresponding items on lists together
    print("========== Products under <= $100 ==========")
    for price in prices:
        if price <= 100:
            print(f"\t{names[index]}\t{IDs[index]}\t{round(prices[index], 2)}")
        index += 1
    # increments after every item


def average(priceList):
    # This function returns the average value of a list
    total = 0
    for price in priceList:
        total += price
    averagePrice = total / len(priceList)
    # Add all list elements together, and then divide by the total number of list elements to get the average
    return averagePrice

def main():
    names = ["Book", "Tea", "Soda", "Shoes", "Mug", "TV"]
    IDs = [100, 101, 102, 103, 104, 105]
    prices = [130, 153, 221, 117, 55, 200]

    # Print the info on all items
    printInfo(names, IDs, prices)

    # Find and print the average
    averagePrice = average(prices)
    print("========================= AVERAGE =========================")
    print(f"The average of prices before the discount is {round(averagePrice, 2)}")

    print("********************************************")
    print("Prices have been adjusted!\n")
    update = discount(prices)
    # Creates a new list with 30% discounted prices

    printInfo(names, IDs, update)
    # Prints the info again, now using the discounted prices

    averagePrice = average(update)
    print("========================= AVERAGE =========================")
    print(f"The average of prices after the discount is {round(averagePrice, 2)}")

    search(names, IDs, update)
    # Finds discounted prices under or equal to $ 100

main()