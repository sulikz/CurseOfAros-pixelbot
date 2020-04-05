import random
import time

import pyautogui

import Player
from Attacker import attack, single_enemy_farmer
from Banker import auto_bank_ore
from Coal_waypoints import move_to_wp0, move_to_random_wp
from FilePaths import Ores
from Miner import miner
from Mobs.Fiends import RockFiend
from Mobs.Raptors import Raptor
from Mover import spawn_to_bank, bank_to_mythan, Mover, bank_to_gold, coal_to_bank, bank_to_coal


def mine_mythan():
    full_inventory, ore_depleted = miner(Ores.Mythan.value)
    rock_fiend = RockFiend()
    if full_inventory:
        # Suicide
        while not Player.check_if_dead():
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
        while not Player.check_if_dead():
            print("Suciding...")
            single_enemy_farmer(Raptor())
        # Move to banka
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
