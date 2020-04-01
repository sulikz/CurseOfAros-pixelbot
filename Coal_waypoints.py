import random
import time

import pyautogui


def move_to_random_wp(current_wp, id):
    if current_wp == 0:
        if id == 0:
            wp0_wp1()
            return 1
        if id == 1:
            wp0_wp2()
            return 2

    elif current_wp == 1:
        if id == 0:
            wp1_wp0()
            return 0
        if id == 1:
            wp1_wp2()
            return 2
    elif current_wp == 2:
        if id == 0:
            wp2_wp0()
            return 0

        if id == 1:
            wp2_wp1()
            return 1


def move_to_wp0(current_wp):
    if current_wp == 1:
        wp1_wp0()
    elif current_wp == 2:
        wp2_wp0()


def wp0_wp1():
    pyautogui.keyDown("s")
    time.sleep(1.1)
    pyautogui.keyUp("s")


def wp0_wp2():
    r = random.uniform(0, 0.85)
    pyautogui.keyDown("d")
    time.sleep(0.85 - r)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(0.85 + r)
    pyautogui.keyUp("d")


def wp1_wp0():
    pyautogui.keyDown("w")
    time.sleep(1.1)
    pyautogui.keyUp("w")


def wp1_wp2():
    r = random.uniform(0, 0.4)
    pyautogui.keyDown("d")
    time.sleep(0.4 - r)
    pyautogui.keyDown("w")
    time.sleep(0.9)
    pyautogui.keyUp("w")
    time.sleep(0.4 + r)
    pyautogui.keyUp("d")
    pyautogui.keyDown("s")
    time.sleep(0.05)
    pyautogui.keyUp("s")


def wp2_wp0():
    r = random.uniform(0, 0.9)
    pyautogui.keyDown("a")
    time.sleep(0.9 - r)
    pyautogui.keyDown("w")
    time.sleep(0.0025)
    pyautogui.keyUp("w")
    time.sleep(0.9 + r)
    pyautogui.keyUp("a")


def wp2_wp1():
    r = random.uniform(0, 0.2)
    pyautogui.keyDown("a")
    time.sleep(0.6 - r)
    pyautogui.keyDown("s")
    time.sleep(1.1)
    pyautogui.keyUp("s")
    # time.sleep(0.4 + r)
    pyautogui.keyUp("a")
