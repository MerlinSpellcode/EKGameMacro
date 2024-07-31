import random
import json
import aiofiles
import os
import asyncio

async def get_async_file():
    current_dir = os.path.dirname(__file__)
    cura_path = os.path.join(current_dir, 'config.json')
    return cura_path

def get_file_path():
    current_dir = os.path.dirname(__file__)
    cura_path = os.path.join(current_dir, 'config.json')
    return cura_path

async def read_cura_spell():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["hp"]["spell"]

async def read_cura_item_vida():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["hp"]["item"]

async def read_cura_item_mana():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["mp"]["item"]

async def read_skill_atk():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data['skill_atk']

async def read_skill_supp():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data['skill_supp']

async def read_food():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["food"]

async def read_granico():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["granico"]

async def read_executioner():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["executioner"]

async def read_ring():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["ring"]

async def read_amulet():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["amulet"]

def read_start_combo():
    cura_path = get_file_path()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["startcombo"]

def read_end_combo():
    cura_path = get_file_path()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["endcombo"]

async def read_target():
    cura_path = await get_async_file()
    with open(cura_path, 'r') as file:
        data = json.load(file)
    return data["target"]


async def rng_gen(intervl):
    return random.randint(intervl[0], intervl[1]) / 1000

async def rng_b(intervl):
    return random.randint(intervl[0], intervl[1])


