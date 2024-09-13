import qrcode
from tkinter import *
from tkinter import ttk
import os

win= Tk()

win.geometry("500x150")

def createQr():
    global entry

    url = entry.get()

    qr = qrcode.QRCode(
            version= 1 ,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size= 6 ,
            border= 3
        )
    img = qr.add_data(url)
    img = qr.make_image()
    os.chdir('../../..')
    with open(os.getcwd()+'/qrcode.png', 'wb') as f:
            img. save(f)
    label1.configure(text="qr-code saved in " + os.getcwd(), fg="green")
    
label=Label(win, text="", font=("Modern 22 bold"))
label.pack()
label.configure(text="Insert the desired url")

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Ok",width= 20, command= createQr).pack(pady=20)

label1=Label(win, text="", font=("Modern 12 bold"))
label1.pack()

win.mainloop()
