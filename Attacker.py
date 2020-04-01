import random
import sys
import time

import numpy as np
import pyautogui
from PIL import ImageGrab

from CheckBox import check_box
from Coordinates import *
from Mover import move_left, move_right, move_down, move_up
import Player


def attack(*color, max_distance=120, min_distance=50, offset=0):
    # Look for color of enemy
    enemy_coords = search_for_color(*color, attack_box=small_search_box_coords)
    if not enemy_coords:
        enemy_coords = search_for_color(*color, attack_box=search_box_coords)
        if not enemy_coords:
            return False
        if Player.check_if_dead():
            return False
    else:
        Player.attack()
    dist_x = player_coords[0] - enemy_coords[0]
    dist_y = player_coords[1] - enemy_coords[1] - offset
    abs_x = abs(player_coords[0] - enemy_coords[0])
    abs_y = abs(player_coords[1] - enemy_coords[1])

    distance = np.sqrt(pow(dist_x, 2) + pow(dist_y, 2))
    direction = check_dir(dist_x, dist_y)
    if distance > max_distance:
        move_to(distance, direction, abs_x, abs_y)

    elif distance > min_distance:
        turn_to(direction, abs_x, abs_y)

    pyautogui.hotkey("w", "s", "a", "d")
    return True


def move_to(distance, direction, abs_x, abs_y):
    t = 1
    if direction == "NW":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("a")
                time.sleep(distance / 400 * t)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("w")
                time.sleep(distance / 300 * t)
                return True
        pyautogui.keyDown("w")
        pyautogui.keyDown("a")
        time.sleep(distance / 350 * t)
    if direction == "NE":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("d")
                time.sleep(distance / 400 * t)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("w")
                time.sleep(distance / 300 * t)
                return True
        pyautogui.keyDown("w")
        pyautogui.keyDown("d")
        time.sleep(distance / 350 * t)
    if direction == "SW":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("a")
                time.sleep(distance / 300 * t)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("s")
                time.sleep(distance / 400 * t)
                return True
        pyautogui.keyDown("s")
        pyautogui.keyDown("a")
        time.sleep(distance / 350 * t)
    if direction == "SE":
        if abs_x > abs_y:
            if abs_y < 150:
                pyautogui.keyDown("d")
                time.sleep(distance / 400 * t)
                return True
        else:
            if abs_x < 150:
                pyautogui.keyDown("s")
                time.sleep(distance / 300 * t)
                return True
        pyautogui.keyDown("s")
        pyautogui.keyDown("d")
        time.sleep(distance / 350 * t)


def turn_to(direction, abs_x, abs_y):
    t = random.uniform(0, 0.1)
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


def search_for_color(*color, attack_box):
    for c in color:
        img = np.asarray(ImageGrab.grab(attack_box).convert('RGB'))
        c = np.asarray(c)
        result = np.where(np.all(img == c, axis=-1))
        if len(result[0] != 0):
            x, y = result[1][0] + attack_box[0], result[0][0] + attack_box[1]
            return x, y
    return False


def auto_heal(percent, potion):
    while Player.check_if_hp(percent):
        Player.drink_potion(potion)


def auto_loot(*items):
    for item in items:
        if check_box(item, use_box_coords):
            pyautogui.click(use_coords)


def last_pos():
    img = np.array(ImageGrab.grab(anti_stuck_coords).convert('RGB'))
    return img
