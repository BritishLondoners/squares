import turtle

def draw_square():
    # Create a turtle object
    t = turtle.Turtle()

    # Draw a square (4 sides)
    for _ in range(4):
        t.forward(100)   # Move forward 100 units
        t.right(90)      # Turn right 90 degrees

    # Keep the window open until clicked
    turtle.done()

# Run the program
draw_square()
