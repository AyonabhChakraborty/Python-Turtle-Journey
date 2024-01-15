import turtle as t

# Set up the Turtle
t.speed(0)  # Set the drawing speed to the fastest
t.bgcolor("black")  # Set the background color to black

# Define colors for the spiral
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a colorful spiral
for i in range(360):
    t.color(colors[i % 4])  # Cycle through the colors
    t.backward(i)  # Move forward by 'i' units
    t.left(279)  # Turn right by 279 degrees

# Close the Turtle Graphics window when clicked
t.exitonclick()