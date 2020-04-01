from multiprocessing import Process

from Attacker import attack
from config import *
from Potion import Potion


def main():
    use_box = ImageGrab.grab(last_item_box_coords)
    use_box.show()
    # bank_to_coal()
    # bank_to_gold()
    # attack(Mobs.RAPTOR.value, attack_box_coords)
    # spawn_to_bank()
    # gold0_gold1()
    # gold1_gold0()
    last_pos = None
    m = Mover()
    bank_to_gold()
    # bank_to_mythan()
    while True:
        # Auto attacker
        # time.sleep(random.uniform(0.1, 0.3))
        # farm_ice_fiends()
        # farm_cave_bats()
        # last_pos = anti_stuck(last_pos)
        # if type(last_pos) == bool:
        #     print("random move")
        #     r = random.randrange(0, 4)
        #     if r == 0:
        #         move_right(0.3)
        #     elif r == 1:
        #         move_up(0.3)
        #     elif r == 2:
        #         move_left(0.3)
        #     elif r == 3:
        #         move_down(0.3)



        # full_auto_farm(raptor_color)
        # farm_forest_fiends()

        mine_gold(m)
        # mine_mythan()

        # Auto smelt
        # smelt_crimsteel()
        # smelt_gold_nuggets()
        # smelt_gold_bar()

        # Auto smith
        # blacksmith(Icons.CrimSteelBarBank.value, Icons.CrimSteelCap.value)


if __name__ == '__main__':
    main()
