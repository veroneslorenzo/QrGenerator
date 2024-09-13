import qrcode
from tkinter import *
from tkinter import ttk

win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

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
    with open('qrcode.png', 'wb') as f:
            img. save(f)
    

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()
label.configure(text="Insert the desired url")

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Ok",width= 20, command= createQr).pack(pady=20)

win.mainloop()
