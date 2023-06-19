from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#from cryptography.fernet import Fernet


#UI
screen = Tk()
screen.title("Secret Notes")
screen.minsize(500, 600)
screen.config(padx=50, pady=50)
FONT = ("Verdana",20,"normal")

#top secret logo
image1 = Image.open("topsecret.png")
topsecret = ImageTk.PhotoImage(image1)
label1 = Label(image=topsecret)
label1.image = topsecret
label1.config(width=1000,height=150)
label1.pack()


def save_and_encrypt():
    title = entry_title.get()
    message = text_message.get("1.0", END)
    master_secret = entry_key.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning("Warning","Please enter all info")
    else:
        #encryp

        with open("secret.txt","a") as datafile:
            datafile.write(f"{text_message}")






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

save_button = Button(text="Save & Encrypt", command=save_and_encrypt)
save_button.pack()

decrypt_button = Button(text="Decrypt")
decrypt_button.pack()

screen.mainloop()