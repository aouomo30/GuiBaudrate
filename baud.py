#import tkinter as tk
import csv
from tkinter import*

def on_click(e):
    #print(seclectOpt.get())
    br_string.set(f'You select {seclectOpt.get()},{secDataOpt.get()},{secParOpt.get()},{secStbOpt.get()}')
    with open("Format.csv", "a", newline="") as f:
        fw = csv.writer(f)
        fw.writerow([{seclectOpt.get()},{secDataOpt.get()},{secParOpt.get()},{secStbOpt.get()}])

root = Tk()
root.option_add("*Font","consolas 20")

root.title('Select Value')
#f1 = Frame(root, bg="blue")
#f1.grid(row=0, column=0)
baudrate = ['1200', '2400', '4800', '9600']
seclectOpt = StringVar()
seclectOpt.set('1200')

DataSize = ['8', '7']
secDataOpt = StringVar()
secDataOpt.set('8')

parity = ['none', 'even', 'odd', 'mark']
secParOpt = StringVar()
secParOpt.set('none')

Stopbit = ['0','1','2']
secStbOpt = StringVar()
secStbOpt.set('1')

br_string = StringVar()

L1 = Label(root, text="Baudrate", width=10)
L1.grid(row=0, column=0)

L2 = Label(root, text="Data Size", width=10)
L2.grid(row=1, column=0)

L3 = Label(root, text="Parity", width=10)
L3.grid(row=2, column=0)

L4 = Label(root, text="Stop Bit", width=10)
L4.grid(row=3, column=0)

#abel(f1, text="", width=10).pack(padx=5, pady=5)
br=OptionMenu(root, seclectOpt, *baudrate)
br.config(width=8)
br.grid(row=0, column=1)

da=OptionMenu(root, secDataOpt, *DataSize)
da.config(width=8)
da.grid(row=1, column=1)

par=OptionMenu(root, secParOpt, *parity)
par.config(width=8)
par.grid(row=2, column=1)

stb=OptionMenu(root, secStbOpt, *Stopbit)
stb.config(width=8)
stb.grid(row=3, column=1)


btn=Button(root,text="Connect", width=10, pady=5)
btn.grid(row=4, column=1)
btn.bind('<Button-1>',on_click)

Label(root, textvariable=br_string, width=30).grid(row=5, columnspan=2)

root.mainloop()

