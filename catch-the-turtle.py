import turtle

board = turtle.Screen()
bg_color = turtle.bgcolor("gray")
board_title = turtle.title("Catch The Turtle")
FONT = ("Arial", 34, "normal")
grid_size = 10

#score
score = turtle.Turtle()

def setup_score_turtle():
    score.penup()
    score.hideturtle()
    score.setpos(0,400)
    score.write(arg="Score: 0", move=False, align="center", font=FONT)



def make_turtle(x,y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size )
    
make_turtle(10,10)
make_turtle(20,20)
make_turtle(30,30)
make_turtle(40,40)

make_turtle(-10,-10)
make_turtle(-20,-20)


setup_score_turtle()

turtle.mainloop()