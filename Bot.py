import time

from FullScripts import *
import keyboard


class Bot(Thread):
    m = Mover()
    running = False

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        # use_box = ImageGrab.grab(use_box_coords)
        # use_box.show()
        # bank_to_gold()
        while True:
            if keyboard.is_pressed('f1') and not self.running:
                self.running = True
                time.sleep(0.5)
            while self.running:
                if keyboard.is_pressed('f1') and self.running:
                    self.running = False
                    time.sleep(0.5)
                # Auto attacker
                # time.sleep(random.uniform(0.1, 0.3))
                farm_rock_fiends()
                # farm_cave_bats()
                # farm_ancient_bats()
                # farm_ice_fiends()
                anti_stuck()
                # farm_cave_bats()

                # pyautogui.keyDown("space")
                # pyautogui.keyUp("space")
                # auto_heal(60, Potion.medium.value)

                # Anti stuck
                # anti_stuck()
                # mine_gold(self.m)
                # mine_mythan()

                # Auto smelt
                # smelt_gold_nuggets()
                # smelt_gold_bar()

    def toggle_run(self):
        if self.running:
            self.running = False
        else:
            self.running = True
