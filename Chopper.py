import time

import numpy as np
import pyautogui
from PIL import ImageGrab

import Player
from Coordinates import *
from Mover import move_right, move_up, move_left, move_down


def check_tree():
    img = np.array(ImageGrab.grab(use_box_coords).convert('RGB'))
    result = np.where(np.all(img == (198, 203, 222), axis=-1))
    if len(result[0] != 0):
        print("Chopping.")
        return True
    else:
        return False


def carve_relic():
    img = np.array(ImageGrab.grab(make_items_box_coords).convert('RGB'))
    result = np.where(np.all(img == (231, 60, 255), axis=-1))
    if len(result[0] != 0):
        x, y = result[1][0], result[0][0]
        pyautogui.click(x, y)
        pyautogui.click(increase_quantity_coords[0], increase_quantity_coords[1], 5, 0.1)
        time.sleep(0.2)
        pyautogui.click(smelt_forge_coords[0],smelt_forge_coords[1])
        return True
    else:
        return False


def pine_to_table():
    move_right(1.25)
    move_up(1.2)
    move_left(0.8)


def table_to_pine():
    move_right(0.8)
    move_down(1.2)
    move_left(1.25)


if __name__ == '__main__':
    while True:
        flag_1 = False
        time.sleep(0.2)
        while not Player.check_full_inventory():
            if check_tree() and not flag_1:
                pyautogui.click((use_box_coords[0], use_box_coords[1]))
                flag_1 = True
            if not check_tree() and flag_1:
                flag_1 = False
        time.sleep(0.3)
        pine_to_table()
        time.sleep(0.3)
        pyautogui.click((use_box_coords[0], use_box_coords[1]))
        time.sleep(0.3)
        carve_relic()
        time.sleep(35)
        time.sleep(0.2)
        table_to_pine()
