import win32gui
import win32ui
import win32con
import ctypes

window_substring = "Projetor Em"

def enum_windows_callback(hwnd, lParam):
    substring, results = lParam
    if substring.lower() in win32gui.GetWindowText(hwnd).lower():
        results.append(hwnd)

def find_window_by_substring(substring):
    results = []
    lParam = (substring, results)
    win32gui.EnumWindows(lambda hwnd, lParam: enum_windows_callback(hwnd, lParam), lParam)
    return results[0] if results else None

def get_pixel_color_from_window(hwnd, x, y):
    left, top, right, bot = win32gui.GetClientRect(hwnd)
    width = right - left
    height = bot - top

    hdc_window = win32gui.GetWindowDC(hwnd)
    hdc_compatible = win32ui.CreateDCFromHandle(hdc_window)
    hdc_memory = hdc_compatible.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(hdc_compatible, width, height)
    hdc_memory.SelectObject(bmp)

    result = ctypes.windll.user32.PrintWindow(hwnd, hdc_memory.GetSafeHdc(), 0)
    if not result:
        raise Exception("Falha ao capturar a janela")

    color = win32gui.GetPixel(hdc_memory.GetSafeHdc(), x, y)
    if color == -1:
        raise Exception("Falha ao obter a cor do pixel")

    r = color & 0xff
    g = (color >> 8) & 0xff
    b = (color >> 16) & 0xff

    hdc_memory.DeleteDC()
    hdc_compatible.DeleteDC()
    win32gui.ReleaseDC(hwnd, hdc_window)
    win32gui.DeleteObject(bmp.GetHandle())

    print(f"R: {r}")
    print(f"G: {g}")
    print(f"B: {b}")

    return (r, g, b)

def chckwndw(x, y, test):
    hwnd = find_window_by_substring(window_substring)
    if hwnd:
        try:
            color = get_pixel_color_from_window(hwnd, x, y)
            return test == color
        except Exception as e:
            print(e)
    else:
        print(f"Janela com o título contendo '{window_substring}' não encontrada.")
