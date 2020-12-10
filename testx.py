from PIL import ImageGrab
import win32gui

hwnd = win32gui.FindWindow(None, r'Cyberpunk 2077 (C) 2020 by CD Projekt RED')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)

image = ImageGrab.grab(dimensions)
image.show()