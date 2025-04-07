"""
Aaron Eberly
March 28, 2025
Demonstrate functions with lists
"""

def usdToEuro(usd):
    # Create a new list with the equivalent euro price of each usd price
    newList = []
    for price in usd:
        price *= .85
        # Coversion rate between usd and euros
        newList.append(price)
        # This new list will be returned to create the list of euro prices
    return newList

def printInfo(usd, euro):
    # Nicely print the USD and euro prices beside each other
    print("\tUSD\tEuro")
    print("==============================")
    # Seperated these printlines to improve readability for the programmer
    index = 0
    for price in usd:
        # I can use usd or euro for this list because they have the same length
        print(f"\t{round(usd[index], 2)}\t{round(euro[index], 2)}")
        index += 1
    print("==============================")
    # This function does not return anything

def average(currency):
    # This will be called twice. Once for usd, and once for euros
    total = 0
    for price in currency:
        total += price
    averagePrice = total / len(currency)
    # Add all list elements together, and then divide by the total number of list elements to get the average
    return averagePrice


def findPrice(usd, euro):
    index = 0
    # Define index so that I can find the euro value that corresponds with the dollar value
    print("Prices in USD and Euro below $50 are:")
    print("\tUSD\tEuro")
    for price in usd:
        if price < 50:
            print(f"\t{round(price, 2)}\t{round(euro[index], 2)}")
        index += 1
        # Makes sure that the item from the euro list always corresponds to the one from the usd list


def main():
    usd = []
    amount = 0
    # Fill up the list until user enters -1
    while amount != -1:
        amount = input("Enter a price in US dollars. Enter -1 to stop: ")
        amount = int(amount)
        if amount > 0:
            usd.append(amount)

    # Count the number of items in the list
    print(f"{len(usd)} prices were entered.")

    # Find and display the averages
    euro = usdToEuro(usd)
    printInfo(usd, euro)
    averageUSD = average(usd)
    averageEuro = average(euro)
    print("============== Averages ==============")
    print(f"The average of the USD prices is {round(averageUSD, 2)}\nThe average of the Euro prices is {round(averageEuro, 2)}")

    # Find prices below $50
    findPrice(usd, euro)

main()
