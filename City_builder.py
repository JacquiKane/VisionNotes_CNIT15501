import turtle
# Since we will be drawing, we must first import the turtle module

yertle = turtle.Turtle()

def drawRectangle(color, coords_x, coords_y, length, height, yertle = yertle):
    # The purpose of this function is to draw a rectangle. 
    # The color, coordinates, and side lengths of the rectangle are specified when the function is called.
    # The last parameter should always be yertle
    sideNumber = 1
    yertle.penup()
    # Make sure to use penup() before moving the turtle so you don't make extra marks
    yertle.goto(coords_x, coords_y)
    yertle.pendown()
    yertle.fillcolor(color)
    yertle.begin_fill()
    for side in range(4):
        # Using modulus here allows you to check which way the turtle is facing. 
        # That way, the code knows whether to use width or height
        if(sideNumber % 2 == 1):
            yertle.forward(length)
        elif(sideNumber % 2 == 0):
            yertle.forward(height)
        yertle.left(90)
        sideNumber += 1
    yertle.end_fill()
    yertle.penup()

def drawOfficeBlock(coords_x, coords_y, width, height, window_side, gap, yertle = yertle):
    #This function creates an office block by specifying where all of the rectangles should be drawn
    drawRectangle("grey", coords_x, coords_y, width, height, yertle)

    #draw door
    door_side = window_side * 2 + gap
    # This means that the width and height of the door will be as wide as two windows and the gap between them
    drawRectangle("black", coords_x + gap, coords_y, door_side, door_side, yertle)

    windowSpacing = window_side + gap
    # adding in this variable makes future calculations simpler.
    numRows = (height - (windowSpacing * 2)) / windowSpacing
    numColumns = (width - gap) / windowSpacing
    # Checks how many rows and columns of windows can fit on the office building. 
    # Don't forget the space taken by the door
    currentX = coords_x + gap
    currentY = height + coords_y - windowSpacing
    numRows = int(numRows)
    numColumns = int(numColumns)
    for row in range(numRows):
        for column in range(numColumns):
            drawRectangle("white", currentX, currentY, window_side, window_side, yertle)
            currentX += windowSpacing
            # After each window is drawn, the turtle moves to the right
        currentY -= windowSpacing
        currentX = coords_x + gap
        # After each row is finished, the turtle resets it's x coordinates, and then moves down to start the next row

def main():
    yertle.speed("fastest")
    drawOfficeBlock(-100, -100, 100, 200, 10, 10, yertle)
    drawOfficeBlock(-80, -120, 120, 160, 20, 5, yertle)
    drawOfficeBlock(110, -50, 300, 300, 40, 20, yertle)
    drawOfficeBlock(0, -70, 60, 120, 5, 10, yertle)
    drawOfficeBlock(40, -50, 140, 200, 18, 15, yertle)
    drawOfficeBlock(-30, -50, 60, 200, 10, 7, yertle)
    # Feel free to experiment with the numbers in the above calls to drawOfficeBlock to see how they change the drawings
    turtle.done()
    # This last line is important so that the drawing window stays open

main()