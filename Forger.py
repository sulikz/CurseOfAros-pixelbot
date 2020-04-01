import random
import sys
import time

import pyautogui

from Banker import click_item, withdraw_item, close_bank, store_item
from CheckBox import check_box
from Coordinates import *
from FilePaths import *
from Mover import *


def forge_item(item):
    # Open up blacksmith when available
    if check_box(UI.UseIcon.value, use_box_coords):
        pyautogui.click(use_coords)
        # Choose item to smelt
        time.sleep(random.uniform(0.3, 0.4))
        click_item(item, 1, make_items_box_coords)
        # Choose quantity
        pyautogui.click(increase_quantity_coords)
        pyautogui.click(increase_quantity_coords)
        # Click Smelt
        time.sleep(random.uniform(0.3, 0.4))
        pyautogui.click(smelt_forge_coords)
        # Wait for completion
        time.sleep(10)
        return True
    return False


def blacksmith(bar, item):
    withdrawn_flag = False
    forged_flag = False
    sold_flag = False

    time.sleep(random.uniform(0.1, 0.3))
    print("Waiting for bank icon to withdraw bars.")
    while not withdrawn_flag:

        if check_box(UI.UseIcon.value, use_box_coords):
            # Open bank
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.click(use_coords)
            # Withdraw hammer
            time.sleep(random.uniform(0.1, 0.3))
            click_item(Icons.HammerBank.value, 1, bank_storage_box_coords)
            # Withdraw bars
            time.sleep(random.uniform(0.1, 0.3))
            if not withdraw_item(bar, 32):
                print("Out of bars.")
                print("Quitting...")
                sys.exit()
            withdrawn_flag = True
            close_bank()

    time.sleep(random.uniform(0.1, 0.3))
    bank_to_anvil()

    print("Waiting for blacksmith icon...")
    while withdrawn_flag and not forged_flag:
        time.sleep(random.uniform(0.1, 0.3))
        forged_flag = forge_item(item)

    time.sleep(random.uniform(0.1, 0.3))
    anvil_to_merchant()

    print("Waiting for merchant icon to sell items")
    while forged_flag and not sold_flag:
        if check_box(UI.UseIcon.value, use_box_coords):
            # Opening trade menu
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.click(use_coords)
            # Choosing item to sell
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.click(merchant_2nd_item_coords)
            # Choosing quantity
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.click(merchant_quantity_coords)
            pyautogui.click(merchant_quantity_coords)
            # Selling
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.click(sell_coords)

            close_bank()
            forged_flag = False
            sold_flag = True
            print("Selling completed")

    print("Moving away from merchant...")
    pyautogui.keyDown("a")
    time.sleep(random.uniform(0.3, 0.4))
    pyautogui.keyUp("a")
