import random
from threading import Thread

from Mover import bank_to_gold, spawn_to_bank, Mover, bank_to_mythan
from config import *
from Potion import Potion
import multiprocessing as mp


def full_auto_farm(mob):
    Thread(target=auto_loot(Loot.MediumPotion.value, Loot.LargePotion.value)).start()
    Thread(target=auto_heal(random.uniform(60, 85), Potion.medium.value)).start()
    Thread(target=auto_heal(25, Potion.large.value)).start()
    Thread(target=attack(mob, 120, offset=50)).start()


def farm_ice_fiends():
    Thread(target=auto_loot(Loot.MediumPotion.value, Loot.LargePotion.value, Loot.GlacialBlade.value)).start()
    Thread(target=auto_heal(random.uniform(60, 85), Potion.medium.value)).start()
    Thread(target=auto_heal(25, Potion.large.value)).start()
    Thread(target=attack(ice_fiend_color, 120, offset=50)).start()


def farm_cave_bats():
    Thread(target=auto_loot(Loot.MediumPotion.value, Loot.LargePotion.value)).start()
    Thread(target=auto_heal(random.uniform(45, 75), Potion.medium.value)).start()
    Thread(target=auto_heal(25, Potion.large.value)).start()
    Thread(target=attack(cave_bat_color, 140, offset=80)).start()


def farm_forest_fiends():
    Thread(target=auto_loot(Loot.MediumPotion.value, Loot.LargePotion.value)).start()
    Thread(target=auto_heal(random.uniform(60, 85), Potion.medium.value)).start()
    Thread(target=auto_heal(25, Potion.large.value)).start()
    Thread(target=attack(forest_fiend, 80, offset=80)).start()


def mine_mythan():
    full_inventory, ore_depleted = miner(Ores.Mythan.value)
    if full_inventory:
        # Suicide
        while not check_if_dead():
            print("Suciding...")
            attack(rock_fiend, 140)
        pyautogui.mouseUp()
        spawn_to_bank()
        auto_bank_ore()
        bank_to_mythan()


def mine_gold(m: Mover):
    time.sleep(random.uniform(0.2, 1))
    full_inventory, ore_depleted = miner(Ores.Gold.value)

    if ore_depleted:
        r = random.uniform(0, 100)
        if m.current_wp == 0 and r < 75:
            m.gold0_gold1()
            m.current_wp = 1
        elif m.current_wp == 1 and r < 75:
            m.gold1_gold0()
            m.current_wp = 0

    if full_inventory:
        # Suicide
        while not check_if_dead():
            print("Suciding...")
            attack(raptor_color, 140)
            pyautogui.hotkey("w", "s", "a", "d")
        # Release keys after attacking
        pyautogui.keyUp("w")
        pyautogui.keyUp("s")
        pyautogui.keyUp("a")
        pyautogui.keyUp("d")
        # Move to bank
        spawn_to_bank()
        # Deposit items
        auto_bank_ore()
        # Move to ore
        bank_to_gold()
        # Reset waypoint
        m.current_wp = 0


def mine_coal(current_wp=0):
    # Auto mine + auto bank
    full_inventory, ore_depleted = miner(Ores.Coal.value)

    if full_inventory:
        # Move to waypoint 0
        move_to_wp0(current_wp)
        # Move to bank
        coal_to_bank()
        # Deposit items
        auto_bank_ore()
        # Move to ore
        bank_to_coal()

    if ore_depleted:
        waypoint = random.randrange(0, 2)
        current_wp = move_to_random_wp(current_wp, waypoint)
    return current_wp
