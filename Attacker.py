import random
import sys
import time

import numpy as np
import pyautogui
from PIL import ImageGrab
from numpy.random.mtrand import randint

import Player
from CheckBox import check_box
from Coordinates import *
from Mobs import Entity
from Mover import move_left, move_right, move_down, move_up, anti_stuck
from Potion import Potion


def single_enemy_farmer(*entity: Entity, small_search_box=small_search_box_coords,
                        search_box=search_box_coords, prioritisation=None):
    i = 0
    j = 0
    dead = False
    while i < 5 and j < 30 and not dead:
        if attack(*entity,
                  search_box=small_search_box):
            pyautogui.keyDown('q')
            i = 0
            j += 1
        Player.use_item()
        auto_heal(35, Potion.large.value)
        auto_heal(random.uniform(50, 75), Potion.medium.value)
        i += 1
        print("i {} j {} ".format(i, j))
        if Player.check_if_dead():
            pyautogui.keyUp('q')
            return False
        if Player.check_if_exp():
            j = 0
    # anti_stuck()
    pyautogui.keyUp('q')
    Player.use_item()
    auto_heal(35, Potion.large.value)
    auto_heal(random.uniform(50, 75), Potion.medium.value)
    if i >= 5:
        attack(*entity,
               search_box=search_box,
               prioritisation=prioritisation)
    if j >= 30:
        sys.exit()
    Player.use_item()
    return True


def attack(*entity: Entity, search_box=search_box_coords, prioritisation=None):
    # Look for color of enemy
    for e in entity:
        enemy_coords = search_for_color(e.color, attack_box=search_box, prioritisation=prioritisation)
        if enemy_coords:
            dist_x = player_coords[0] - enemy_coords[0]
            dist_y = player_coords[1] - enemy_coords[1] - e.offset
            abs_x = abs(player_coords[0] - enemy_coords[0])
            abs_y = abs(player_coords[1] - enemy_coords[1])

            distance = np.sqrt(pow(dist_x, 2) + pow(dist_y, 2))
            direction = check_dir(dist_x, dist_y)
            if distance > e.max_distance:
                move_to(distance, direction, abs_x, abs_y)

            elif e.max_distance > distance > e.min_distance:
                turn_to(direction, abs_x, abs_y)
            return True
    return False


def move_to(distance, direction, abs_x, abs_y):
    t = 0.8
    if direction == "NW":
        if abs_x > abs_y:
            if abs_y < 100:
                pyautogui.keyDown("a")
                time.sleep(distance / 400 * t)
                pyautogui.keyUp("a")
                return True
        else:
            if abs_x < 100:
                pyautogui.keyDown("w")
                time.sleep(distance / 300 * t)
                pyautogui.keyUp("w")
                return True
        pyautogui.keyDown("w")
        pyautogui.keyDown("a")
        time.sleep(distance / 350 * t)
        pyautogui.keyUp("w")
        pyautogui.keyUp("a")
    if direction == "NE":
        if abs_x > abs_y:
            if abs_y < 100:
                pyautogui.keyDown("d")
                time.sleep(distance / 400 * t)
                pyautogui.keyUp("d")
                return True
        else:
            if abs_x < 100:
                pyautogui.keyDown("w")
                time.sleep(distance / 300 * t)
                pyautogui.keyUp("w")
                return True
        pyautogui.keyDown("w")
        pyautogui.keyDown("d")
        time.sleep(distance / 350 * t)
        pyautogui.keyUp("w")
        pyautogui.keyUp("d")
    if direction == "SW":
        if abs_x > abs_y:
            if abs_y < 100:
                pyautogui.keyDown("a")
                time.sleep(distance / 300 * t)
                pyautogui.keyUp("a")
                return True
        else:
            if abs_x < 100:
                pyautogui.keyDown("s")
                time.sleep(distance / 400 * t)
                pyautogui.keyUp("s")
                return True
        pyautogui.keyDown("s")
        pyautogui.keyDown("a")
        time.sleep(distance / 350 * t)
        pyautogui.keyUp("s")
        pyautogui.keyUp("a")
    if direction == "SE":
        if abs_x > abs_y:
            if abs_y < 100:
                pyautogui.keyDown("d")
                time.sleep(distance / 400 * t)
                pyautogui.keyUp("d")
                return True
        else:
            if abs_x < 100:
                pyautogui.keyDown("s")
                time.sleep(distance / 300 * t)
                pyautogui.keyUp("s")
                return True
        pyautogui.keyDown("s")
        pyautogui.keyDown("d")
        time.sleep(distance / 350 * t)
        pyautogui.keyUp("s")
        pyautogui.keyUp("d")


def turn_to(direction, abs_x, abs_y):
    t = random.uniform(0, 0.05)
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


def search_for_color(color: list, attack_box, prioritisation=None):
    for c in color:
        i = ImageGrab.grab(attack_box)
        # i.show()
        img = np.asarray(i.convert('RGB'))
        c = np.asarray(c)
        result = np.where(np.all(img == c, axis=-1))
        if len(result[0] != 0):
            if prioritisation == "random":
                print('yes')
                r = randint(len(result[0]))  # Randomizing enemy searching instead of prioritising top left -> bot right
            else:
                r = 0
            x, y = result[1][r] + attack_box[0], result[0][r] + attack_box[1]
            return x, y
    return False


def auto_heal(percent, potion):
    while Player.check_if_hp(percent):
        Player.drink_potion(potion)
        time.sleep(0.1)


def auto_loot(*items):
    for item in items:
        if check_box(item, use_box_coords):
            pyautogui.click(use_coords)
