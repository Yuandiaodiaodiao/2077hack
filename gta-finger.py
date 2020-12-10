import cv
import win32api
import win32con
import time
import getscreen
import getPicture
import ctypes
import multiprocessing
import os
import json
if not os.path.exists("config.json"):
    with open("config.json",'w')as f:
        json.dump({
            "resolution":"1920x1080",
            "screenmode":"window",
            "keycooldown":0.01,
            "pointcooldown":2.5
        },f)

# MODE = "window"
# FULLRES = [1920, 1080]
LEFT = 65
DOWN = 83
UP = 87
RIGHT = 68
# keycooldown = 0.01
# pointcooldown = 2.5
with open("config.json","r")as f:

    js=json.load(f)
    MODE=js["screenmode"]
    x,y=map(int,js["resolution"].strip().split("x"))
    FULLRES=[x,y]
    keycooldown=js["keycooldown"]
    pointcooldown=js["pointcooldown"]
import cv2

import threading


def press(key,cooldown=keycooldown):
    MapKey = ctypes.windll.user32.MapVirtualKeyA
    win32api.keybd_event(key, MapKey(key, 0), 0, 0)
    time.sleep(cooldown)
    win32api.keybd_event(key, MapKey(key, 0), win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(keycooldown)

from pynput.keyboard import Listener
from time import sleep
def breakonce(i):
    global MODE
    press(74)
    sleep(0.3)
    press(UP)
    sleep(0.1)
    press(13)
    print("回车")
    time.sleep(1.5)
    #菜单出现


    for j in range(2,i+1):
        print("down")
        press(DOWN)
        sleep(0.01)
    #偷
    print("回车2")
    press(13)
    sleep(0.3)
    press(UP)
    sleep(0.02)
    press(13)
    sleep(0.5)
    press(13)
    sleep(0.3 )
    press(13)



import gtapoint

f11thread = None

def money():
    while True:
        press(LEFT, 5)
        press(RIGHT, 7)
        sleep(3)
        press(LEFT, 1)
        sleep(3)
thread1=None
def presskey(key):
    global FULLRES
    global MODE
    global f11thread
    global pointcooldown
    if not hasattr(key, "name"):
        return

    if key.name=="f11":
        global thread1
        if thread1 is not None:
            if thread1.is_alive():
                thread1.terminate()
            thread1=None
        else:
            thread1=multiprocessing.Process(target=money)
            thread1.start()



    if key.name == "f10":
        breakonce(1)
    elif key.name == "f9":
        breakonce(2)
    elif key.name == "f8":
        breakonce(3)
    elif key.name == "f7":
        breakonce(4)
    elif key.name=="f6":
        press(27)
        press(UP)
        press(UP)
        press(UP)
        press(13)
        press(DOWN)
        press(DOWN)
        press(13)
        time.sleep(0.3)
        press(UP)
        press(13)
        sleep(6)
        press(13)
        sleep(0.5)
        press(13)
        sleep(3)
        # press(UP)
        press(13)
        sleep(0.3)
        press(UP)
        press(13)
    else:
        return


if __name__ == "__main__":

    with Listener(on_press=presskey) as listener:
        listener.join()
