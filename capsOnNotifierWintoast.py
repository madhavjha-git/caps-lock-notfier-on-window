from win10toast import ToastNotifier
import keyboard
from win32api import GetKeyState 
from win32con import VK_CAPITAL 

def capture_key(e):
    if e.name == "caps lock":
        if (GetKeyState(VK_CAPITAL) & 0x0001) !=0 :
            toaster.show_toast("Caps lock On"," ",  threaded=True,icon_path='C:\\win.ico', duration=1 )
        else:
            toaster.show_toast("Caps lock Off"," ",threaded=True,icon_path='C:\\win.ico', duration=1)

toaster = ToastNotifier()

keyboard.on_release(callback=capture_key, suppress=False)
keyboard.wait()