import time
from threading import Thread

from Attacker import auto_heal
from FullScripts import *
import keyboard

from Mover import anti_stuck
from Potion import Potion


class Bot(Thread):
    m = Mover()
    running = False

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        # use_box = ImageGrab.grab(small_search_box_coords)
        # use_box.show()
        time.sleep(2)
        bank_to_gold()
        while True:
            if keyboard.is_pressed('f1') and not self.running:
                self.running = True
                time.sleep(0.5)
            while self.running:
                # Auto attacker
                # farm_rock_fiends()
                # farm_luminant_slimes()
                # farm_cave_bats()
                # farm_ice_raptors()
                # if not single_enemy_farmer():
                #     print("Exiting")
                    # sys.exit()
                # farm_ice_fiends()
                # farm_cave_bats()
                # auto_heal(35, Potion.large.value)
                # auto_heal(random.uniform(50, 75), Potion.medium.value)

                # anti_stuck()
                mine_gold(self.m)
                # mine_mythan()

                # Auto smelt
                # smelt_gold_nuggets()
                # smelt_gold_bar()
                # if Player.check_if_dead():
                #     self.running = False
                if keyboard.is_pressed('f1') and self.running:
                    self.running = False
                    time.sleep(0.5)

    def toggle_run(self):
        if self.running:
            self.running = False
        else:
            self.running = True
