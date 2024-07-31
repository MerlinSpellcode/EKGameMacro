import asyncio
import json
from src.utils.aux_func import rng_gen, read_food, rng_b
from src.winobs import chckwndw
from src.press import *


food_interval = (33000, 34000)
food_mini = (111, 222)

async def use_food(cast_spell):
    while not chckwndw(cast_spell):
        await a_press_btn(cast_spell["hk"])
        await asyncio.sleep(await rng_gen(food_mini))

async def loop_food():
    food = await read_food()
    while True:
        try:
            for s in food:
                await a_press_btn(s)
                await asyncio.sleep(await rng_gen(food_mini))
            await asyncio.sleep(await rng_gen(food_interval))
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
        await asyncio.sleep(await rng_gen(food_interval))
