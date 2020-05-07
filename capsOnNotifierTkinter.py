
import keyboard
from win32api import GetKeyState 
from win32con import VK_CAPITAL 
from tkinter import *


def capture_key(e):
    if e.name == "caps lock":
        if (GetKeyState(VK_CAPITAL) & 0x0001) !=0 :
            e1.delete(0, END)
            e1.insert(END, "On")
        else:
            e1.delete(0, END)
            e1.insert(END, 'Off')

window=Tk()
window.wm_title("Caps Lock Status")
title_text = StringVar()

l1 = Label(window, text='Caps Lock')
l1.grid(row=0, column=0)

e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

keyboard.on_release(callback=capture_key, suppress=False)

window.mainloop()