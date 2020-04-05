import random
import sys
import time

import pyautogui
from PIL import ImageGrab

from CheckBox import check_box
from Coordinates import *
from FilePaths import UI


def auto_bank_ore():
    print("Waiting for bank...")
    if check_box(UI.UseIcon.value, use_box_coords):
        time.sleep(0.1)
        pyautogui.click(use_coords)
        time.sleep(0.2)
        print("Depositing item in last slot...")
        for _ in range(36):
            time.sleep(random.uniform(0.01, 0.1))
            pyautogui.click(last_item_coords)
        print("Ores transferred to bank.")
        close_bank()

    return True


def click_item(item, quantity, location):
    for i in range(quantity):
        window = ImageGrab.grab(location)
        found = pyautogui.locate(item, window, confidence=0.9)
        print(found)
        if found:
            x, y, w, h = found
            time.sleep(random.uniform(0.01, 0.02))
            pyautogui.click(x + location[0], y + location[1])
        else:
            return False
    return True


def store_item(item, quantity):
    print("Storing...")
    return click_item(item, quantity, item_storage_box_coords)


def withdraw_item(item, quantity):
    print("Withdrawing...")
    return click_item(item, quantity, bank_storage_box_coords)


def close_bank():
    time.sleep(0.1)
    pyautogui.click(bank_exit_coords)
