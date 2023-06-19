from tkinter import *

#UI
screen = Tk()
screen.title("Secret Notes")
screen.minsize(500, 600)
screen.config(padx=75, pady=75)
FONT = ("Verdana",20,"normal")

photo = PhotoImage(file="topsecret.jpg")
photo_label = Label(image=photo)
photo_label.pack()



title = Label(text="Enter Your Title", font=FONT)
title.pack()

entry_title = Entry(width=50)
entry_title.pack()

message = Label(text="Enter Your Message",font=FONT)
message.pack()

text_message = Text()
text_message.pack()

key = Label(text="Enter Your Master Key",font=FONT)
key.pack()

entry_key = Entry()
entry_key.pack()

save_button = Button(text="Save & Encrypt")
save_button.pack()

decrypt_button = Button(text="Decrypt")
decrypt_button.pack()


screen.mainloop()