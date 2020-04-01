import random

from Banker import click_item, withdraw_item, store_item, close_bank
from CheckBox import check_box
from Coordinates import *
from FilePaths import UI, Icons
from Mover import *


def smelt_crimsteel():
    smelt_steel(Icons.CrimSteelBarSmelter, Icons.CrimSteelBarInventory,
                Icons.CrimSteelIconBank.value, 18,
                Icons.CoalIconBank.value, 18)


def smelt_gold_nuggets():
    return smelt_steel(Icons.GoldNuggetSmelter.value, Icons.GoldNuggetInventory.value,
                       Icons.GoldOreIconBank.value, 32, wait_time=3, smelt_quantity=2)


def smelt_gold_bar():
    return smelt_steel(Icons.GoldBarSmelter.value, Icons.GoldBarInventory.value,
                       Icons.GoldNuggetBank.value, 20, wait_time=2, smelt_quantity=1)


def smelt_steel(bar_smelter_icon, bar_inventory_icon, ore_1, quantity_1, ore_2=None, quantity_2=0, wait_time=10,
                smelt_quantity=10):
    withdrawn_flag = False
    smelt_flag = False
    enough_withdrawn = False

    time.sleep(random.uniform(0.3, 0.4))
    print("Waiting for bank icon to withdraw items")
    while not withdrawn_flag:
        if check_box(UI.UseIcon.value, use_box_coords):
            time.sleep(random.uniform(0.3, 0.4))
            pyautogui.click(use_coords)
            time.sleep(random.uniform(0.3, 0.4))
            enough_withdrawn = withdraw_item(ore_1, quantity_1)
            if ore_2:
                withdraw_item(ore_2, quantity_2)
            withdrawn_flag = True
            close_bank()
        if not enough_withdrawn:
            return False

    time.sleep(random.uniform(0.3, 0.4))
    bank_to_smelter()

    print("Waiting for smelter icon...")
    while withdrawn_flag and not smelt_flag:
        time.sleep(random.uniform(0.3, 0.4))
        smelt_flag = smelt_item(bar_smelter_icon, wait_time)

    time.sleep(random.uniform(0.3, 0.4))
    smelter_to_bank()

    print("Waiting for bank icon to store items")
    while smelt_flag:
        if check_box(UI.UseIcon.value, use_box_coords):
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.click(use_coords)
            smelt_flag = False
    time.sleep(random.uniform(0.1, 0.3))
    stored_flag = store_item(bar_inventory_icon, smelt_quantity)
    if stored_flag:
        print("Smelting completed")
    close_bank()
    return stored_flag


def smelt_item(item, wait_time):
    # Open up smelter when available
    if check_box(UI.Smelt.value, use_box_coords):
        pyautogui.click(use_coords)

        # Choose bar to smelt
        time.sleep(random.uniform(0.3, 0.4))
        click_item(item, 1, make_items_box_coords)

        # Choose quantity
        pyautogui.click(increase_quantity_coords)
        pyautogui.click(increase_quantity_coords)

        # Click Smelt
        time.sleep(random.uniform(0.3, 0.4))
        pyautogui.click(smelt_forge_coords)

        # Wait for completion
        time.sleep(wait_time)
        return True
    return False
