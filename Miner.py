import random
import time

import numpy as np
import pyautogui
from PIL import ImageGrab

from CheckBox import check_box
from Coordinates import *


def miner(ore):
    ore_depleted = True
    full_inventory = False

    print("Waiting for ore...")
    while ore_depleted:
        ore_depleted = mine_ore(ore)

    while not full_inventory and not ore_depleted:
        # Check if ore has been depleted
        ore_depleted = check_ore_status()

        # Check if inventory is full
        full_inventory = check_full_inventory()

    return full_inventory, ore_depleted


def mine_ore(ore):
    if check_box(ore, use_box_coords):
        time.sleep(random.uniform(0.2, 0.4))
        print("Mining ore...")
        pyautogui.click(use_coords)
        time.sleep(random.uniform(2.5, 3))
        return False
    else:
        return True


def check_full_inventory():
    img = np.array(ImageGrab.grab(inv_full_box_coords).convert('RGB'))
    r, g, b = img[0][0]
    if r == 255 and g == 255 and b == 0:
        print("Inventory full. Go to bank.")
        return True
    else:
        return False


def check_ore_status():
    img = np.array(ImageGrab.grab(ore_depleted_box_coords).convert('RGB'))
    r, g, b = img[0][0]
    if r == 255 and g == 0 and b == 0:
        print("Ore is depleted.")
        return True
    else:
        return False
