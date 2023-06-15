import tkinter

screen = tkinter.Tk()
screen.title("Tkiner Python")
screen.minsize(500,600)

def button_clicked():
    data = "Hello World!"
    label.config(text=data)


button = tkinter.Button(text="Say Hi",command=button_clicked)
button.config(
    fg="red"
)
button.pack()

label = tkinter.Label(screen, text="")
label.pack()


tkinter.mainloop()
