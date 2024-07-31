import pyautogui as pg
pg.FAILSAFE= False

def press_btn(hk):
    pg.press(hk)

async def a_press_btn(hk):
    pg.press(hk)