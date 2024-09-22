import turtle

'''WE HAVE DEFINED A FUNCTION THAT TAKES USER INPUTS SO IT CAN 
   DRAW THE CAKE AND TABLE AS PER USER REQUIREMENTS'''


def questions():
    color_of_table = input("What is the color of your table: ")
    
    sizeofcake = int(input("Enter a number between 10 and 100 for leg height: "))
    lengthofonesideoftable = int(input("Enter a number between 10 and 100 for the side length: "))
    
    return color_of_table, sizeofcake, lengthofonesideoftable

def cake_dimensions():
    base_width = int(input("Enter base width of the cake (between 115 and 120): "))
    while base_width < 115 or base_width > 120:
        base_width = int(input("Invalid input. Enter base width of the cake (between 115 and 120): "))

    base_height = int(input("Enter base height of the cake (between 28 and 30): "))
    while base_height < 28 or base_height > 30:
        base_height = int(input("Invalid input. Enter base height of the cake (between 28 and 30): "))

    middle_width = int(input("Enter middle width of the cake (between 95 and 100): "))
    while middle_width < 95 or middle_width > 100:
        middle_width = int(input("Invalid input. Enter middle width of the cake (between 95 and 100): "))

    middle_height = int(input("Enter middle height of the cake (between 28 and 30): "))
    while middle_height < 28 or middle_height > 30:
        middle_height = int(input("Invalid input. Enter middle height of the cake (between 28 and 30): "))

    top_width = int(input("Enter top width of the cake (between 75 and 80): "))
    while top_width < 75 or top_width > 80:
        top_width = int(input("Invalid input. Enter top width of the cake (between 75 and 80): "))

    top_height = int(input("Enter top height of the cake (between 28 and 30): "))
    while top_height < 28 or top_height > 30:
        top_height = int(input("Invalid input. Enter top height of the cake (between 28 and 30): "))
    
    return base_width, base_height, middle_width, middle_height, top_width, top_height

def draw_table(color_of_table, sizeofcake, lengthofonesideoftable):
    turtle.speed(10)
    turtle.fillcolor(color_of_table)
    turtle.begin_fill()

    # We are drawing the table top
    turtle.penup()
    turtle.goto(-lengthofonesideoftable / 2 - 10, 0)
    turtle.pendown()

    turtle.forward(lengthofonesideoftable + 20)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(lengthofonesideoftable + 20)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)

    turtle.end_fill()

    # we are drawing the legs
    leg_height = sizeofcake
    leg_width = 10
    leg_positions = [
        (-lengthofonesideoftable / 2 + 5, -30),
        (lengthofonesideoftable / 2 + 5, -30),
        (-lengthofonesideoftable / 2 + 5, -30 - leg_height),
        (lengthofonesideoftable / 2 + 5, -30 - leg_height)
    ]

    for x, y in leg_positions:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color_of_table)
        turtle.begin_fill()
        turtle.setheading(-90)
        turtle.forward(leg_height)
        turtle.right(90)
        turtle.forward(leg_width)
        turtle.right(90)
        turtle.forward(leg_height)
        turtle.right(90)
        turtle.forward(leg_width)
        turtle.right(90)
        turtle.end_fill()
        turtle.setheading(0)

    turtle.hideturtle()

def draw_cake(base_width, base_height, middle_width, middle_height, top_width, top_height):
    # Draw the base layer of the cake
    turtle.penup()
    turtle.goto(-base_width / 2, 20)
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()

    turtle.forward(base_width)
    turtle.right(90)
    turtle.forward(base_height)
    turtle.right(90)
    turtle.forward(base_width)
    turtle.right(90)
    turtle.forward(base_height)
    turtle.right(90)
    turtle.end_fill()

    # Draw the middle layer of the cake
    turtle.penup()
    turtle.goto(-middle_width / 2, 20 + base_height)
    turtle.pendown()
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.forward(middle_width)
    turtle.right(90)
    turtle.forward(middle_height)
    turtle.right(90)
    turtle.forward(middle_width)
    turtle.right(90)
    turtle.forward(middle_height)
    turtle.right(90)
    turtle.end_fill()

    # Draw the top layer of the cake
    turtle.penup()
    turtle.goto(-top_width / 2, 20 + base_height + middle_height)
    turtle.pendown()
    turtle.fillcolor("skyblue")
    turtle.begin_fill()
    turtle.forward(top_width)
    turtle.right(90)
    turtle.forward(top_height)
    turtle.right(90)
    turtle.forward(top_width)
    turtle.right(90)
    turtle.forward(top_height)
    turtle.right(90)
    turtle.end_fill()

    # We are setting positions based on the top layer height
    top_layer_y = 20 + base_height + middle_height + top_height

    # We are fixing cherry positions here
    cherry_positions = [
        (0, top_layer_y - 30),  # Center cherry
        (-15, top_layer_y - 35),  # Left of center
        (15, top_layer_y - 35)   # Right of center
    ]
    for position in cherry_positions:
        turtle.penup()
        turtle.goto(position)
        turtle.pendown()
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

    # Candle
    turtle.penup()
    turtle.goto(5, top_layer_y -30) 
    turtle.setheading(180)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.forward(10)  
    turtle.right(90)
    turtle.forward(30)  
    turtle.right(90)
    turtle.forward(10)  
    turtle.right(90)
    turtle.forward(30)  
    turtle.end_fill()

    # We are drawing a candle flame here
    turtle.penup()
    turtle.goto(1, top_layer_y)  
    turtle.setheading(0)  
    turtle.pendown()
    turtle.fillcolor("orange")  
    turtle.begin_fill()
    turtle.circle(5)  
    turtle.end_fill()

def main():
    color_of_table, sizeofcake, lengthofonesideoftable = questions()
    base_width, base_height, middle_width, middle_height, top_width, top_height = cake_dimensions()
    
    draw_table(color_of_table, sizeofcake, lengthofonesideoftable)
    draw_cake(base_width, base_height, middle_width, middle_height, top_width, top_height)

    input("Press key to exit")

main()