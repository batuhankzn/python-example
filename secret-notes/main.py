from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import base64


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

    crypted = encode(master_secret,message)

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning("Warning","Please enter all info")
    else:
        try:
            with open(f"{title}.txt","a") as datafile:
                datafile.write(f"{crypted}")
        except FileNotFoundError:
            with open(f"{title}.txt","w") as datafile:
                datafile.write(f"{crypted}")
        finally:
            entry_title.delete(0,END)
            text_message.delete(1.0,END)
            entry_key.delete(0,END)

def decrypt_notes():
    message = text_message.get("1.0", END)
    master_secret = entry_key.get()

    if len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning("Warning","Please enter all info")
    else:
        try:
            decrypted_message = decode(master_secret,message)
            text_message.delete(1.0,END)
            text_message.insert(1.0,decrypted_message)
        except:
            messagebox.showwarning("Warning","Please enter encrypted text!")


#encrypt and decrypt
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


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

decrypt_button = Button(text="Decrypt", command=decrypt_notes)
decrypt_button.pack()

screen.mainloop()