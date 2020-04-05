from threading import Thread

from Attacker import attack
from Potion import Potion
from config import *


def full_auto_farm(mob):
    auto_loot(Loot.MediumPotion.value, Loot.LargePotion.value)
    auto_heal(random.uniform(60, 85), Potion.medium.value)
    auto_heal(25, Potion.large.value)
    attack(mob, 120, offset=50)


def farm_cave_bats():
    Player.use_item()
    auto_heal(random.uniform(45, 75), Potion.medium.value)
    auto_heal(25, Potion.large.value)
    attack(cave_bat_color, 140, offset=110)


def farm_luminant_slimes():
    Player.use_item()
    auto_heal(35, Potion.large.value)
    auto_heal(random.uniform(50, 75), Potion.medium.value)
    attack(luminant_slime_hit_1,
           luminant_slime_1,
           luminant_slime_2,
           max_distance=100,
           min_distance=80,
           offset=0)


def farm_ice_raptors():
    single_enemy_farmer(ice_raptor_1, min_distance=70)


def farm_ancient_bats():
    return single_enemy_farmer(ancient_bat_1, max_distance=140, min_distance=80, offset=90, prioritisation="random")
    # attack(ancient_bat_hit_1,
    #        ancient_bat_hit_2,
    #        ancient_bat_1,
    #        ancient_bat_hit_2,
    #        max_distance=140,
    #        min_distance=80,
    #        offset=80,
    #        search_box=ancient_bat_search_coords)


def farm_forest_fiends():
    auto_loot(Loot.MediumPotion.value, Loot.LargePotion.value)
    auto_heal(random.uniform(60, 85), Potion.medium.value)
    auto_heal(25, Potion.large.value)
    attack(forest_fiend, 80, offset=80)


def farm_rock_fiends():
    return single_enemy_farmer(rock_fiend, max_distance=140, min_distance=80, offset=50)
    # Player.use_item()
    # auto_heal(25, Potion.large.value)
    # auto_heal(random.uniform(50, 75), Potion.medium.value)
    # attack(rock_fiend, rock_fiend_hit, 140, min_distance=80, offset=50)


def farm_ice_fiends():
    Player.use_item()
    auto_heal(25, Potion.large.value)
    auto_heal(random.uniform(50, 75), Potion.medium.value)
    attack(ice_fiend_color, 100, min_distance=60, offset=50)


def mine_mythan():
    full_inventory, ore_depleted = miner(Ores.Mythan.value)
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
            single_enemy_farmer(raptor_color, max_distance=160, min_distance=100)
            # pyautogui.hotkey("w", "s", "a", "d")
        # Release keys after attacking
        # pyautogui.keyUp("w")
        # pyautogui.keyUp("s")
        # pyautogui.keyUp("a")
        # pyautogui.keyUp("d")
        # Move to bankasa
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
