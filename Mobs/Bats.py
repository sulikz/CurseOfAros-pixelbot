from abc import ABC

from Mobs.Entity import Entity


class BatEntity(Entity, ABC):

    def __init__(self):
        self.max_distance = 140
        self.min_distance = 80
        self.offset = 90


class Bat(BatEntity):

    def __init__(self):
        super().__init__()
        self.color = (222, 207, 57)


class CaveBat(BatEntity):

    def __init__(self):
        super().__init__()
        self.color = (181, 142, 82)


class AncientBat(BatEntity):

    def __init__(self):
        super().__init__()
        self.color = (57, 56, 82)
