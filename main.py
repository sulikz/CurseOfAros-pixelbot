import queue
from multiprocessing import Process

from Attacker import attack
from config import *
from Potion import Potion


def main():
    # use_box = ImageGrab.grab(small_search_box_coords)
    # use_box.show()
    # bank_to_coal()
    # bank_to_gold()
    # attack(Mobs.RAPTOR.value, attack_box_coords)
    # spawn_to_bank()
    # gold0_gold1()
    # gold1_gold0()
    stuck_list = []

    m = Mover()
    # bank_to_gold()
    # bank_to_mythan()
    while True:
        # Auto attacker
        # time.sleep(random.uniform(0.1, 0.3))
        farm_ice_fiends()
        print("loop")
        # farm_cave_bats()
        anti_stuck()
        # attacking = farms_rock_fiends()
        # full_auto_farm(raptor_color)

        # Anti stuck


        # full_auto_farm(raptor_color)
        # farm_forest_fiends()

        # mine_gold(m)
        # mine_mythan()

        # Auto smelt
        # smelt_crimsteel()
        # smelt_gold_nuggets()
        # smelt_gold_bar()

        # Auto smith
        # blacksmith(Icons.CrimSteelBarBank.value, Icons.CrimSteelCap.value)


if __name__ == '__main__':
    main()
