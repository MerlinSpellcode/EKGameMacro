import asyncio
from pynput import keyboard
from src.cura import *
from src.food import loop_food
from src.skill import *

def on_press(key):
    try:
        if key.char == '=':
            toggle_skill_loop()
        if key.char == '-':
            toggle_heal_loop()
    except AttributeError:
        pass

async def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    await asyncio.gather(
        loop_magia_cura(),
        loop_item_cura(),
        loop_food(),
        loop_target(),
        loop_skill_atk(),
        loop_skill_supp()
    )

asyncio.run(main())
