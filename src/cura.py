import asyncio
import json
from src.utils.aux_func import *
from src.winobs import chckwndw
from src.press import *

toggle_heal_active = False
item_interval = (900, 950)
interval = (100, 200)
spell_spam = (20, 200)

def toggle_heal_loop():
    global toggle_heal_active
    toggle_heal_active = not toggle_heal_active
    print(f"Cura {'ativado' if toggle_heal_active else 'desativado'}")

async def use_item_vida(item_vida):
    global toggle_heal_active
    while not chckwndw(item_vida):
        if toggle_heal_active:
            await a_press_btn(item_vida["hk"])
            await asyncio.sleep(await rng_gen(item_interval))

async def use_item_mana(item_mana, item_vida):
    global toggle_heal_active
    while not chckwndw(item_mana):
        if toggle_heal_active:
            if chckwndw(item_vida):
                await a_press_btn(item_mana["hk"])
                await asyncio.sleep(0.1)
            else:
                break

async def use_ring():
    data_ring = await read_ring()
    if not chckwndw(data_ring["life"]) and not chckwndw(data_ring["slot"]):
        await a_press_btn(data_ring["hk"])
        await asyncio.sleep(0.05)

async def use_amulet():
    data_amulet = await read_amulet()
    if not chckwndw(data_amulet["life"]) and not chckwndw(data_amulet["slot"]):
        await a_press_btn(data_amulet["hk"])
        await asyncio.sleep(0.05)

async def loop_item_cura():
    global toggle_heal_active
    item_vida = await read_cura_item_vida()
    item_mana = await read_cura_item_mana()
    while True:
        try:
            if toggle_heal_active:
                if not chckwndw(item_vida["strong"]):
                    await use_ring()
                    await use_amulet()
                    await use_item_vida(item_vida["strong"])
                elif not chckwndw(item_vida["light"]):
                    await use_item_vida(item_vida["light"])
                elif not chckwndw(item_mana["light"]):
                    await use_item_mana(item_mana["light"], item_vida["strong"])
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
        await asyncio.sleep(await rng_gen(interval))

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

async def cast_new_spell(cast_spell):
    while not chckwndw(cast_spell):
        await a_press_btn(cast_spell["hk"])
        await asyncio.sleep(await rng_gen(spell_spam))

async def loop_magia_cura():
    global toggle_heal_active
    spell = await read_cura_spell()
    while True:
        try:
            if toggle_heal_active:
                if not chckwndw(spell["light"]):
                    await cast_new_spell(spell["light"])
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
        await asyncio.sleep(0.1)


