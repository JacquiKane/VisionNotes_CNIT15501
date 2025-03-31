"""
Aaron Eberly
Feb 11, 2025
Demo for loops
"""

import random
import turtle
yertle = turtle.Turtle()
yertle.pensize(10)

def main():
    for colorPick in ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
        yertle.pencolor(colorPick)
        yertle.circle(50)

    turtle.done
main()