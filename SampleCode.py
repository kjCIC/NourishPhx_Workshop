# Calling the turtle library for use
import turtle

# Giving the turtle a name
t = turtle.Turtle()

# Setting drawing speed
t.speed(3)

# Setting background color
t.screen.bgcolor("lightblue")

# Changing the size of the turtle window
turtle.setup(600, 600)

# Function for a square
def my_square():
    # Using a 'for' loop to go forward and right 4 times (making a square)
    # This eliminates the need to write (t.forward.. t.right.. so many times)
    for x in range(4):
        t.forward(50)
        t.right(90)
        
# Function for a triangle
def my_triangle():
    # Using a 'for' loop to go forward and right 3 times (making a triangle)
    for x in range(3):
        t.forward(50)
        t.right(120)

# Making sure the pen is down
t.pendown()

# Picking up the pen and moving it to a specific spot
t.penup()
t.goto(100, 200)
t.pendown()

# The yellow sun
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
# Turtle has a built-in function to make circles, the number changes the size
t.circle(30)
t.end_fill()

# Moving the pen back to the center
t.pencolor("black")
t.penup()
t.goto(0, 0)
t.pendown()

# The red square
# The fill color is red
t.fillcolor("red")
# Beginning the fill
t.begin_fill()
# Calling the square function (placing the square here)
my_square()
# Ending the fill here
t.end_fill()

# Angling the pen to make the triangle
t.left(60)

#  The blue triangle
t.fillcolor("blue")
t.begin_fill()
# Calling the triangle function (placing the triangle here)
my_triangle()
t.end_fill()

# Picking the pen up and changing the color, moving it back to center
t.penup()
t.pencolor("black")
t.goto(0, 0)

# Reorienting the pen- this is trial and error!
t.right(60)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(30)

# Starting the door with the color pink
# Going around the right side of the house
# Feel free to experiment with this until you get it right
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.right(90)
t.forward(30)
t.right(90)
t.forward(10)
t.right(90)
t.forward(30)
t.right(90)
t.forward(10)
t.end_fill()

# Picking up the pen and changing the color
t.penup()
t.pencolor("green")

# Moving the turtle to the left side of the screen to start the grass
t.goto(-300, -50)
t.pendown()
t.fillcolor("green")
t.begin_fill()
# Beginning the fill & completing the rectangle for the grass
t.backward(600)
t.right(90)
t.backward(250)
t.right(90)
t.backward(600)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Telling the turtle it is done drawing
turtle.done()

# See if you can add a window, a doorknob, and a cloud (& any more details you'd like)
