import win32gui
import win32ui
import win32con
import win32api
from PIL import Image
from pynput import mouse, keyboard

def get_pixel_color(x, y):
    hdc = win32gui.GetDC(0)
    try:
        color = win32gui.GetPixel(hdc, x, y)
        r = color & 0xff
        g = (color >> 8) & 0xff
        b = (color >> 16) & 0xff
        return (r, g, b)
    finally:
        win32gui.ReleaseDC(0, hdc)

def chckwndw(check):
    color = get_pixel_color(check["x"], check["y"])
    color_to_check = (check["color"][0], check["color"][1], check["color"][2])
    # print("@@@@@@@@@@@@")
    # print([check["color"][0], check["color"][1], check["color"][2]])
    # print(color)
    # print(color_to_check)
    # print("@@@@@@@@@@@@")
    return color == color_to_check

# def executth(check):
#     color = get_pixel_color(check["x"], check["y"])
#     color_to_check = (check["color"][0], check["color"][1], check["color"][2])
#     print("@@@@@@@@@@@@")
#     print(color)
#     print(color_to_check)
#     print("@@@@@@@@@@@@")
#     return color == color_to_check


