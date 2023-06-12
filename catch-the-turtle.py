import turtle

board = turtle.Screen()
bg_color = turtle.bgcolor("gray")
board_title = turtle.title("Catch The Turtle")
FONT = ("Arial", 34, "normal")
grid_size = 10

#game board
gameBoard = turtle.Turtle()
gameBoard.shapesize(3,3)
gameBoard.hideturtle()
gameBoard.penup()
gameBoard.goto(-450,450)
gameBoard.pendown()
gameBoard.goto(450,450)
gameBoard.goto(450,-450)
gameBoard.goto(-450,-450)
gameBoard.goto(-450,450)



#score
score = turtle.Turtle()

def setup_score_turtle():
    score.penup()
    score.hideturtle()
    score.setpos(0,400)
    score.write(arg="Score: 0", move=False, align="center", font=FONT)


#make turtle
def make_turtle(x,y):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size )
    

# 1 and 2 area
make_turtle(0,0)
make_turtle(25,0)
make_turtle(40,0)
make_turtle(0,35)
make_turtle(0,20)
make_turtle(-25,0)
make_turtle(-40,0)

#1
make_turtle(30,27)
make_turtle(33,19)
make_turtle(15,13)
make_turtle(15,32)

#2
make_turtle(-30,27)
make_turtle(-33,19)
make_turtle(-15,13)
make_turtle(-15,32)


# 3 and 4 area
make_turtle(0,-22)

#3
make_turtle(-30,-27)
make_turtle(-33,-19)
make_turtle(-15,-13)
make_turtle(-15,-32)

#4
make_turtle(30,-27)
make_turtle(33,-19)
make_turtle(15,-13)
make_turtle(15,-32)






setup_score_turtle()

turtle.mainloop()