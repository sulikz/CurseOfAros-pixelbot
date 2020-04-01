import random
import sys
import time

import numpy as np
import pyautogui
from PIL import ImageGrab

from CheckBox import check_box
from Coordinates import *
from Mover import move_left, move_right, move_down, move_up


def attack(color, max_distance=120, offset=0):
    # Look for color of enemy
    enemy_coords = search_for_color(color, small_search_box_coords, 15)
    if not enemy_coords:
        pyautogui.hotkey("w", "s", "a", "d")
        pyautogui.mouseUp()

    while not enemy_coords:
        enemy_coords = search_for_color(color, search_box_coords, step=50)
        if check_if_dead():
            return False
    dist_x = player_coords[0] - enemy_coords[0]
    dist_y = player_coords[1] - enemy_coords[1] - offset
    abs_x = abs(player_coords[0] - enemy_coords[0])
    abs_y = abs(player_coords[1] - enemy_coords[1])

    distance = np.sqrt(pow(dist_x, 2) + pow(dist_y, 2))
    direction = check_dir(dist_x, dist_y)
    if distance > max_distance:
        move_to(distance, direction, abs_x, abs_y)

        pyautogui.mouseDown(attack_box_coords[0], attack_box_coords[1])
    else:
        pyautogui.mouseDown(attack_box_coords[0], attack_box_coords[1])
        pyautogui.hotkey("w", "s", "a", "d")
        turn_to(direction, abs_x, abs_y)
    #     print("Quitting...")
    #     sys.exit()


def move_to(distance, direction, abs_x, abs_y):
    if direction == "NW":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("a")
                time.sleep(distance / 400 * 0.6)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("w")
                time.sleep(distance / 300 * 0.6)
                return True
        pyautogui.keyDown("w")
        pyautogui.keyDown("a")
        time.sleep(distance / 350 * 0.8)
    if direction == "NE":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("d")
                time.sleep(distance / 400 * 0.6)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("w")
                time.sleep(distance / 300 * 0.6)
                return True
        pyautogui.keyDown("w")
        pyautogui.keyDown("d")
        time.sleep(distance / 350 * 0.8)
    if direction == "SW":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("a")
                time.sleep(distance / 300 * 0.6)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("s")
                time.sleep(distance / 400 * 0.6)
                return True
        pyautogui.keyDown("s")
        pyautogui.keyDown("a")
        time.sleep(distance / 350 * 0.6)
    if direction == "SE":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("d")
                time.sleep(distance / 400 * 0.6)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("s")
                time.sleep(distance / 300 * 0.6)
                return True
        pyautogui.keyDown("s")
        pyautogui.keyDown("d")
        time.sleep(distance / 350 * 0.6)


def turn_to(direction, abs_x, abs_y):
    t = 0.1
    if direction == "NW":
        if abs_x > abs_y:
            move_left(t)
        else:
            move_up(t)
    elif direction == "NE":
        if abs_x > abs_y:
            move_right(t)
        else:
            move_up(t)
    elif direction == "SW":
        if abs_x > abs_y:
            move_left(t)
        else:
            move_down(t)
    elif direction == "SE":
        if abs_x > abs_y:
            move_right(t)
        else:
            move_down(t)


def check_dir(dist_x, dist_y):
    if dist_x > 0 and dist_y > 0:
        return "NW"
    if dist_x < 0 and dist_y > 0:
        return "NE"
    if dist_x > 0 and dist_y < 0:
        return "SW"
    if dist_x < 0 and dist_y < 0:
        return "SE"
    # if dist_y > 0 : N  || if dist_y < 0 : S
    # if dist_x > 0 : W  || if dist_x < 0 : E


def search_for_color(color, attack_box, step=10):
    img = np.asarray(ImageGrab.grab(attack_box).convert('RGB'))
    color = np.asarray(color)
    result = np.where(np.all(img == color, axis=-1))
    if len(result[0] != 0):
        x, y = result[1][0] + attack_box[0], result[0][0] + attack_box[1]
        return x, y
    else:
        return False


def check_if_dead():
    img = np.array(ImageGrab.grab(player_dead_coords).convert('RGB'))
    r, g, b = img[0][0]
    if r == 255 and g == 0 and b == 0:
        print("Player died")
        return True
    else:
        return False


def check_if_hp(percent):
    # HP = x <350, 850>
    x = (percent * 500 / 100) + 350
    y = 133
    img = np.array(ImageGrab.grab((x, y, x + 1, y + 1)).convert('RGB'))
    r, g, b = img[0][0]
    if r == 123 and g == 101 and b == 82:
        return True
    else:
        return False


def drink_potion(potion):
    pyautogui.click(potion[0], potion[1])


def auto_heal(percent, potion):
    while check_if_hp(percent):
        drink_potion(potion)


def auto_loot(*items):
    for item in items:
        if check_box(item, use_box_coords):
            pyautogui.click(use_coords)


def anti_stuck(last_pos):
    img = np.array(ImageGrab.grab(anti_stuck_coords).convert('RGB'))
    if (last_pos == img).all():
        return False
    else:
        return img
