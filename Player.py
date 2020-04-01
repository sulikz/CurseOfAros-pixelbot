import numpy as np
import pyautogui
from PIL import ImageGrab
from Coordinates import *


def attack():
    pyautogui.click(attack_box_coords[0], attack_box_coords[1])


def use_item():
    pyautogui.click(use_box_coords[0], use_box_coords[1])


def drink_potion(potion):
    pyautogui.click(potion[0], potion[1])


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

