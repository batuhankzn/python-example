import turtle

board = turtle.Screen()
bg_color = turtle.bgcolor("#75E6DA")
board_title = turtle.title("First Turtle Example")


#square
'''
turtle1 = turtle.Turtle()
for i in range(4):
    turtle1.forward(100)
    turtle1.left(90)
'''

#polygon

turtle2 = turtle.Turtle()

num_sides = 7
angle = 360 / num_sides
side_lenght = 100

for i in range(num_sides):
    turtle2.right(angle)
    turtle2.forward(side_lenght)



turtle.done()