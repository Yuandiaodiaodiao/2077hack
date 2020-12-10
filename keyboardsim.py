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
    # press(DOWN)
    # time.sleep(1)
    # press(72)
    # import pyautogui
    #
    # pyautogui.moveTo(x=100, y=100, duration=2, tween=pyautogui.linear)
    # pyautogui.press('esc')
    from pydamo_0 import Time, DM, Mouse, Key, vk

    dm = DM()
    # dm.reg_infos.unreg_dm()
    # dm.dm.SetSimMode(ord('1'))
    ms = Mouse(dm)
    kk = Key(dm)
    import win32gui
    # hwnd = win32gui.FindWindow(None, r'Cyberpunk 2077 (C) 2020 by CD Projekt RED')
    # print(hwnd)
    # dm.BindWindow(hwnd,"normal","normal","normal",0)

    tt = Time()
    tt.sleep(1)
    kk.down(vk.enter)  # 按下a键
    tt.sleep(0.25)
    kk.up(vk.enter)