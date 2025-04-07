"""
Aaron Eberly
April 3, 2025
Demonstrate functions with lists
"""

import copy
# This must be imported so that a deep copy can be done later

def getRoomsFromDB():
    # This function initializes the list of rooms
    return [[100, 101, 102, 103, 104], [204, 205], [306, 307, 308, 309, 310], [411, 412, 413, 414, 415, 416, 417, 418, 419, 420], [521]]

def initRooms(rooms):
    # A deep copy makes sure that the layout of the list is preserved, but does not point back to the original list
    occupiedRooms = copy.deepcopy(rooms)
    for floorIndex in range(len(occupiedRooms)):
        for roomIndex in range(len(occupiedRooms[floorIndex])):
            occupiedRooms[floorIndex][roomIndex] = False

    return occupiedRooms

def processReservation(rooms, occupiedRooms):
    # This function will mark a room as reserved
    prettyPrintRooms(rooms, occupiedRooms)

    # The list availableRooms will have every room that is not reserved in a 1d list.
    availableRooms = getRooms(rooms, occupiedRooms, True)
    roomToReserve = input("\nPlease enter the room number to reserve:")
    roomToReserve = int(roomToReserve)

    if not(roomToReserve in listAllRooms(rooms)):
        print("You seem to have entered an invalid room number")
        # This checks to see if the room exists in the hotel
    elif not(roomToReserve in availableRooms):
        # This checks to make sure that the room is available
        print("Sorry - that room is occupied, please choose a room, that is not currently occupied.")
    else:
        print(f"Your room {roomToReserve} is reserved")
        floor, room = locate(roomToReserve, rooms)
        occupiedRooms[floor][room] = True
        # Update the parallel list to mark the room as reserved

    prettyPrintRooms(rooms, occupiedRooms)

def listAllRooms(rooms):
    # This creates a 1d list from a 2d list, allowing certain functions such as "in" to be effective
    allRooms = []
    for i in rooms:
        for j in i:
            allRooms.append(j)
    return allRooms

def getRooms(rooms, occupiedRooms, stay):
    # This either lists all reserved rooms or all unreserved rooms, depending upon the value of the boolean variable stay
    roomsList = []
    for floorIndex in range(len(occupiedRooms)):
        for roomIndex in range(len(occupiedRooms[floorIndex])):
            if stay:
                if (not(occupiedRooms[floorIndex][roomIndex])):
                    roomsList.append(rooms[floorIndex][roomIndex])
            else:
                if(occupiedRooms[floorIndex][roomIndex]):
                    roomsList.append(rooms[floorIndex][roomIndex])
    return roomsList

def locate(roomNumber, rooms):
    # This function returns the index of the chosen room in the 2d list.
    floor = int(roomNumber/100)
    floor -= 1
    if (roomNumber in rooms[floor]):
        roomIndex = rooms[floor].index(roomNumber)
        return floor, roomIndex

def processCheckout(rooms, occupiedRooms):
    # In many ways, this function is very similar to processReservation, but backwards
    bookedRooms = getRooms(rooms, occupiedRooms, False)
    roomToVacate = input("\nPlease enter the room number to vacate:")
    roomToVacate = int(roomToVacate)

    if not(roomToVacate in listAllRooms(rooms)):
        print("You seem to have entered an invalid room number")
    elif not(roomToVacate in bookedRooms):
        print("Sorry - this room isn't occupied.")
    else:
        print(f"You have checked the client out of room {roomToVacate}")
        floorIndex, roomIndex = locate(roomToVacate, rooms)
        occupiedRooms[floorIndex][roomIndex] = False

    prettyPrintRooms(rooms, occupiedRooms)

def prettyPrintRooms(rooms, occupiedRooms):
    # This function makes sure the printed room layout looks nice
    for floor in range(len(rooms)):
        print(f"\nFloor {floor + 1}: ", end = "")
        for roomNum in range(len(rooms[floor])):
            showRoom = rooms[floor][roomNum] if not(occupiedRooms[floor][roomNum]) else f"X-{rooms[floor][roomNum]}"
            print(f"[{showRoom}]", end = "")

def main():
    # Initialize the list of hotelRooms
    hotelRooms = getRoomsFromDB()

    # Deep copy a parallel list that will track whether each room is reserved.
    occupiedRooms = initRooms(hotelRooms)
    processingReservations = True
    # processingReservations only turns false when the option to exit the program is selected.
    while processingReservations:
        print(f"\nSelect\n\t(1) Book a room\n\t(2) Check out, or\n\t(3) Exit the system")
        action = int(input("\nEnter your choice, 1, 2, or 3:"))
        if action == 1:
            print("Booking")
            processReservation(hotelRooms, occupiedRooms)
        elif action == 2:
            print("Checkout")
            processCheckout(hotelRooms, occupiedRooms)
        elif action == 3:
            processingReservations = False
            # This will cause the menu loop to end

main()