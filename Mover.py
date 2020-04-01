import queue
import random
import time

import pyautogui

import Attacker
from Attacker import *
from Coordinates import use_box_coords


class Mover:
    current_wp = 0

    def gold0_gold1(self):
        r = random.uniform(0, 1)
        move_down(1.1 - r, release=False)
        move_right(0.25)
        move_down(2.2 + r)
        move_right(0.6)
        self.current_wp = 1

    def gold1_gold0(self):
        move_left(0.6)
        r = random.uniform(0, 1)
        move_up(2.2 + r, release=False)
        move_left(0.2)
        move_up(1.05 - r)
        move_left(0.15)
        self.current_wp = 0


def move_up(t, release=True):
    pyautogui.keyDown("w")
    time.sleep(t)
    if release:
        pyautogui.keyUp("w")
    print("up {}".format(t))


def move_down(t, release=True):
    pyautogui.keyDown("s")
    time.sleep(t)
    if release:
        pyautogui.keyUp("s")
    print("down {}".format(t))


def move_left(t, release=True):
    pyautogui.keyDown("a")
    time.sleep(t)
    if release:
        pyautogui.keyUp("a")
    print("left {}".format(t))


def move_right(t, release=True):
    pyautogui.keyDown("d")
    time.sleep(t)
    if release:
        pyautogui.keyUp("d")
    print("right {}".format(t))


def bank_to_anvil():
    print("Moving to anvil...")
    pyautogui.keyDown("d")
    time.sleep(3)
    pyautogui.keyUp("d")

    pyautogui.keyDown("w")
    time.sleep(0.2)
    pyautogui.keyUp("w")

    pyautogui.keyDown("d")
    time.sleep(1.8)
    pyautogui.keyUp("d")

    pyautogui.keyDown("w")
    time.sleep(0.7)
    pyautogui.keyUp("w")

    pyautogui.keyDown("a")
    time.sleep(0.6)
    pyautogui.keyUp("a")


def anvil_to_merchant():
    print("Moving to merchant...")
    pyautogui.keyDown("d")
    time.sleep(0.3)
    pyautogui.keyUp("d")

    pyautogui.keyDown("s")
    time.sleep(0.7)
    pyautogui.keyUp("s")

    pyautogui.keyDown("a")
    time.sleep(1.7)
    pyautogui.keyDown("s")
    time.sleep(0.22)
    pyautogui.keyUp("s")
    time.sleep(1.9)
    pyautogui.keyUp("a")

    pyautogui.keyDown("w")
    time.sleep(0.1)
    pyautogui.keyUp("w")


def bank_to_smelter():
    print("Moving to anvil...")
    pyautogui.keyDown("d")
    time.sleep(3)
    pyautogui.keyUp("d")

    pyautogui.keyDown("w")
    time.sleep(0.2)
    pyautogui.keyUp("w")

    pyautogui.keyDown("d")
    time.sleep(1.8)
    pyautogui.keyUp("d")

    pyautogui.keyDown("w")
    time.sleep(1.2)
    pyautogui.keyUp("w")


def smelter_to_bank():
    print("Moving to bank...")
    pyautogui.keyDown("s")
    time.sleep(1.25)
    pyautogui.keyUp("s")

    pyautogui.keyDown("a")
    time.sleep(2)
    pyautogui.keyDown("s")
    time.sleep(0.19)
    pyautogui.keyUp("s")
    time.sleep(2)
    pyautogui.keyUp("a")

    pyautogui.keyDown("w")
    time.sleep(0.1)
    pyautogui.keyUp("w")


def bank_to_coal():
    print("Moving to coal ore...")
    pyautogui.keyDown("d")
    time.sleep(0.5)
    pyautogui.keyDown("s")
    time.sleep(2.5)
    pyautogui.keyUp("s")
    time.sleep(1)
    pyautogui.keyUp("d")

    pyautogui.keyDown("s")
    time.sleep(1)
    pyautogui.keyDown("d")
    time.sleep(0.3)
    pyautogui.keyUp("d")
    time.sleep(2)
    pyautogui.keyUp("s")

    pyautogui.keyDown("d")
    time.sleep(0.5)
    pyautogui.keyDown("s")
    time.sleep(2.1)
    pyautogui.keyUp("s")
    time.sleep(2.5)
    pyautogui.keyUp("d")

    pyautogui.keyDown("s")
    time.sleep(0.2)
    pyautogui.keyUp("s")

    pyautogui.keyDown("d")
    time.sleep(0.8)
    pyautogui.keyUp("d")

    pyautogui.keyDown("w")
    time.sleep(0.2)
    pyautogui.keyUp("w")


def coal_to_bank():
    pyautogui.keyDown("a")
    time.sleep(2)
    pyautogui.keyDown("w")
    time.sleep(5)
    pyautogui.keyUp("w")
    time.sleep(0.5)
    pyautogui.keyUp("a")

    pyautogui.keyDown("w")
    time.sleep(2)
    pyautogui.keyDown("a")
    time.sleep(2)
    pyautogui.keyUp("a")
    time.sleep(0.1)
    pyautogui.keyUp("w")

    pyautogui.keyDown("a")
    time.sleep(1)
    pyautogui.keyUp("a")

    pyautogui.keyDown("w")
    time.sleep(0.2)
    pyautogui.keyUp("w")


def bank_to_gold():
    r = random.uniform(0, 0.5)
    move_left(3 - r, release=False)
    move_down(2)
    move_left(0 + r)
    r = random.uniform(0, 1.5)
    move_left(3 - r, release=False)
    randomize("v")
    move_left(2 + r)
    move_down(1, release=False)
    move_left(0.5)
    move_down(2, release=False)
    move_left(0.5)
    r = random.uniform(0, 1)
    move_down(2 - r, release=False)
    randomize("h")
    move_down(1.5, release=False)
    move_left(0.5)
    move_down(3, release=False)
    move_left(1)
    move_down(2.5)
    r = random.uniform(0, 1)
    move_left(2 - r, release=False)
    move_up(1.5)
    move_left(1 + r)
    move_left(1.6)
    move_down(0.0001)
    r = random.randrange(2)
    if r == 1:
        move_left(0.0001)


def spawn_to_bank():
    move_down(0.5)
    move_right(2.5)
    move_up(0.7)


def randomize(mode):
    r = random.uniform(0, 0.2)
    if mode == "h":
        move_left(r)
        time.sleep(random.uniform(0, 0.2))
        move_right(r)
    if mode == "v":
        move_up(r)
        time.sleep(random.uniform(0, 0.2))
        move_down(r)


def bank_to_mythan():
    move_right(2, release=False)
    move_up(0.2)
    move_right(5, release=False)
    move_up(3.5)
    move_right(3.5, release=False)
    move_up(1)
    move_right(0.5)
    move_up(2)
    pyautogui.click(use_box_coords[0], use_box_coords[1])
    time.sleep(0.3)
    # Cave entered
    move_up(2.8)
    move_left(2.1)
    move_down(2.1)


last_p = None
positions = queue.Queue(10)


def anti_stuck():
    last_p = Attacker.last_pos()
    if positions.full():
        positions.get()
        positions.put(last_p)
        array = np.asarray(positions.queue)
        if (last_p == array).all():
            print("stuck")
            r = random.randrange(0, 4)
            if r == 0:
                move_right(0.3)
            elif r == 1:
                move_up(0.3)
            elif r == 2:
                move_left(0.3)
            elif r == 3:
                move_down(0.3)
    else:
        positions.put(last_p)

