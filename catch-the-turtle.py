import turtle

board = turtle.Screen()
bg_color = turtle.bgcolor("#75E6DA")
board_title = turtle.title("Catch The Turtle")
FONT = ("Arial", 34, "normal")

#score
score = turtle.Turtle()

def setup_score_turtle():
    score.penup()
    score.hideturtle()
    score.setpos(0,400)
    score.write(arg="Score: 0", move=False, align="center", font=FONT)



setup_score_turtle()

turtle.mainloop()