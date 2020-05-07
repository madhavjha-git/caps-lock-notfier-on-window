import keyboard
from plyer import notification
from win32api import GetKeyState 
from win32con import VK_CAPITAL 

def capture_key(e):
    if e.name == "caps lock":
        if (GetKeyState(VK_CAPITAL) & 0x0001) !=0 :
            notification.notify(title='Caps On',message=" ",app_icon='C:\\win.ico',timeout=1)
        else:
            notification.notify(title='Caps Off',message=" ",app_icon='C:\\win.ico',timeout=1)

keyboard.on_release(callback=capture_key, suppress=False)
keyboard.wait() 