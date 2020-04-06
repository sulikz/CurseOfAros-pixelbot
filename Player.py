import time

import numpy as np
import pyautogui
from PIL import ImageGrab
from Coordinates import *


def attack():
    pyautogui.hotkey('q')


def use_item():
    pyautogui.hotkey('e')


def drink_potion(potion):
    if potion == 1:
        pyautogui.hotkey('1')
    if potion == 2:
        pyautogui.hotkey('2')
    if potion == 3:
        pyautogui.hotkey('3')


def check_full_inventory():
    img = np.array(ImageGrab.grab(inv_full_box_coords).convert('RGB'))
    r, g, b = img[0][0]
    if r == 255 and g == 255 and b == 0:
        print("Inventory full. Go to bank.")
        return True
    else:
        return False


def check_if_dead():
    img = np.array(ImageGrab.grab(player_dead_coords).convert('RGB'))
    r, g, b = img[0][0]
    if r == 255 and g == 0 and b == 0:
        print("Player died")
        return True
    else:
        return False


def check_if_hp(percent):
    # HP = x <350, 850>
    x = (percent * 500 / 100) + 350
    y = 133
    img = np.array(ImageGrab.grab((x, y, x + 1, y + 1)).convert('RGB'))
    r, g, b = img[0][0]
    if r == 123 and g == 101 and b == 82:
        return True
    else:
        return False


def check_if_exp():
    img = np.array(ImageGrab.grab(player_exp_coords).convert('RGB'))
    yellow = np.asarray((255, 255, 0))
    result = np.where(np.all(img == yellow, axis=-1))
    if len(result[0] != 0):
        print('killed')
        return True
    else:
        return False
