import time
import ctypes
import win32api
import win32con
keycooldown=0.01
LEFT=37
UP=38
RIGHT=39
DOWN=40
ENTER=13
def press(key,cooldown=keycooldown):
    MapKey = ctypes.windll.user32.MapVirtualKeyA
    win32api.keybd_event(key, MapKey(key, 0), 0, 0)
    time.sleep(cooldown)
    win32api.keybd_event(key, MapKey(key, 0), win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(cooldown)

if __name__=="__main__":
    press(DOWN)
