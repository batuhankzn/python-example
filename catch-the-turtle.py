import turtle
import random

board = turtle.Screen()
bg_color = turtle.bgcolor("gray")
board_title = turtle.title("Catch The Turtle")
FONT = ("Arial", 34, "normal")
grid_size = 10
scoreB = 0


#game board
def gameBoard_setup():
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



#score board
score = turtle.Turtle()

def setup_score_turtle():
    score.penup()
    score.hideturtle()
    score.setpos(0,400)
    score.write(arg="Score: 0", move=False, align="center", font=FONT)


#make turtle
def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global scoreB
        scoreB += 1
        score.clear()
        score.write(arg=f"Score: {scoreB}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.speed(0)
    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size )
    turtle_list.append(t)
    

def setup_turtles():
    x_coordinates = [-30,-20,-10,0,10,20,30]
    y_coordinates = [30,20,10,0,-10,-20,-30]

    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)
    


#turtles hide            
turtle_list = []
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#show only 1 turtle
def show_turtles():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    turtle.ontimer(show_turtles,500)




#fonctions 
turtle.tracer(0)


setup_turtles()
setup_score_turtle()
hide_turtles()
show_turtles()



turtle.tracer(1)
gameBoard_setup()
turtle.mainloop()