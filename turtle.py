import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color

# Initialize the turtle
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to maximum

# Define colors for the squares
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw a pattern of colorful squares
for i in range(36):  # Draw 36 squares
    pen.color(colors[i % len(colors)])  # Set the color of the square
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.begin_fill()
    for _ in range(4):  # Draw the square
        pen.forward(100)
        pen.left(90)
    pen.end_fill()
    pen.right(10)  # Rotate the turtle for the next square

# Hide the turtle and display the drawing
pen.hideturtle()
turtle.done()
