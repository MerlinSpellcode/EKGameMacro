import asyncio
import random
from src.winobs import *
import json
from src.utils.aux_func import *
from src.press import *

skill_loop_active = False
spam_interval = (100, 150)
setup_combo_interval = (200, 350)
skill_interval = (1900, 1950)

def press_setup_keys(keys):
    for key in keys:
        press_btn(key)
        tempo = random.randint(setup_combo_interval[0], setup_combo_interval[1]) / 1000
        asyncio.run(asyncio.sleep(0.2))  # Micro intervalo entre as teclas

def toggle_skill_loop():
    global skill_loop_active
    skill_loop_active = not skill_loop_active
    if not skill_loop_active:
        press_setup_keys(read_end_combo())
    else:
        press_setup_keys(read_start_combo())
    print(f"Loop_skill {'ativado' if skill_loop_active else 'desativado'}")

async def granico():
    skill_granico = await read_granico()
    if chckwndw(skill_granico):
        await a_press_btn(skill_granico["hk"])
        await asyncio.sleep(2)
        return True
    else:
        return False
    
async def executioner():
    return True
    # data_executioner = await read_executioner()
    # if chckwndw(data_executioner["check_mob"]):
    #     if chckwndw(data_executioner["check_life"]):
    #         if chckwndw(data_executioner["skill"]):
    #             await a_press_btn(data_executioner["skill"]["hk"])
    #             await asyncio.sleep(2)
    #             await a_press_btn("SPACE")
    #             await asyncio.sleep(await rng_gen(spam_interval))

async def loop_skill_atk():
    global skill_loop_active
    skills = await read_skill_atk()
    cooldowns = {}
    while True:
        if skill_loop_active:
            for skill in skills:
                tecla = skill["hk"]
                if skill_loop_active:
                    await a_press_btn("SPACE")
                    await asyncio.sleep(await rng_gen(spam_interval))
                    await executioner()
                    if skill["cond"]:
                        if not await granico() and skill_loop_active:
                            await a_press_btn(tecla)
                            await asyncio.sleep(2)
                    else:
                        if skill_loop_active:
                            await a_press_btn(tecla)
                            await asyncio.sleep(2)  
        await asyncio.sleep(0.01)

async def loop_target():
    global skill_loop_active
    data_target = await read_target()
    tecla = data_target["hk"]
    while True:
        if skill_loop_active:
            if not chckwndw(data_target):
                await a_press_btn(tecla)
                await asyncio.sleep(0.2)
        await asyncio.sleep(0.1)

async def loop_skill_supp():
    global skill_loop_active
    skills = await read_skill_supp()
    cooldowns = {}
    while True:
        if skill_loop_active:
            for skill in skills:
                tecla = skill["hk"]
                cooldown = skill["time"]
                if tecla not in cooldowns or cooldowns[tecla] <= 0:
                    cooldowns[tecla] = cooldown / 1000  # Armazenar cooldown em segundos
                    await a_press_btn(tecla)
                    await asyncio.sleep(1.9)  # Sleep após cada input
                cooldowns = {k: v-0.1 for k, v in cooldowns.items()}  # Atualiza cooldowns
        await asyncio.sleep(0.1)
