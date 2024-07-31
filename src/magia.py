import asyncio
import json
from src.utils.aux_func import rng_gen, read_cura_spell, rng_b
from src.winobs import chckwndw
from src.press import *


spell_spam = (20, 200)
interval = (10, 20)

# spell_interval = (850, 1093)
# async def cast_spell(spell_hk):
#     b = await rng_b(1,100)
#     if b > 70:
#         repeat = await rng_b(2, 6)
#         for _ in range(repeat):
#             press_btn(spell_hk)
#             await asyncio.sleep(await rng_gen(interval))
#     else:
#         press_btn(spell_hk)
#     await asyncio.sleep(await rng_gen(spell_interval))

async def cast_new_spell(cast_spell):
    while not chckwndw(cast_spell):
        await a_press_btn(cast_spell["hk"])
        await asyncio.sleep(await rng_gen(spell_spam))

async def loop_magia():
    spell = await read_cura_spell()
    while True:
        try:
            if not chckwndw(spell["light"]):
                await cast_new_spell(spell["light"])
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
        await asyncio.sleep(await rng_gen(interval))
