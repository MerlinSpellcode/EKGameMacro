import win32gui
import win32ui
import win32con
import win32api
from PIL import Image
from pynput import mouse, keyboard

def get_pixel_color(x, y):
    # Get the desktop's device context (DC)
    hdc = win32gui.GetDC(0)
    try:
        # Get the color of the pixel
        color = win32gui.GetPixel(hdc, x, y)
        # Extract the RGB components
        r = color & 0xff
        g = (color >> 8) & 0xff
        b = (color >> 16) & 0xff
        return (r, g, b)
    finally:
        # Release the device context
        win32gui.ReleaseDC(0, hdc)

def on_click(x, y, button, pressed):
    if pressed:
        color = get_pixel_color(x, y)
        print(f"A cor do pixel em ({x}, {y}) é {color}")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            btn = key.char.upper()
        else:
            btn = str(key).split('.')[1].upper()
        
        if btn == 'ESC':
            return False
        
        # Get current mouse position
        x, y = win32api.GetCursorPos()
        color = get_pixel_color(x, y)
        
        print(f'{{"x": {x}, "y": {y}, "color": [{color[0]}, {color[1]}, {color[2]}], "hk": "{btn}"}}')
    except AttributeError:
        pass

# Start listening to mouse and keyboard events
keyboard_listener = keyboard.Listener(on_press=on_press)

keyboard_listener.start()

keyboard_listener.join()
