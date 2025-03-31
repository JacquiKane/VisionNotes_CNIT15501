import turtle

# Create a turtle object, draw speedily!
yertle = turtle.Turtle()
yertle.speed("fastest")

def main():
    x = -180
    y = 180
    for flowerrow in range(3):
        for flower in range(3):
            # Draw 6 red petals
            yertle.fillcolor("red")
            yertle.penup()
            yertle.goto(x, y)
            yertle.pendown()
            petal_count = 1
            while (petal_count <= 6):
                yertle.begin_fill()
                yertle.circle(100, 60)
                yertle.left(120)
                yertle.circle(100, 60)
                yertle.left(120)
                yertle.end_fill()
                # rotate
                yertle.left(60)
                petal_count += 1

            # Draw 8 smaller yellow petals centered in the middle of the pink petals
            yertle.penup()
            yertle.goto(x, y)
            yertle.pendown()
            yertle.fillcolor("yellow")
            petal_count = 1
            while (petal_count <= 8):
                yertle.begin_fill()
                yertle.circle(50, 60)
                yertle.left(120)
                yertle.circle(50, 60)
                yertle.left(120)
                yertle.end_fill()
                yertle.left(45)
                petal_count += 1
            x += 180
        x = -180
        y -= 180

            # Hide the turtle (optional), keep displaying window
    yertle.hideturtle()
    turtle.done()

main()

# iffyloops