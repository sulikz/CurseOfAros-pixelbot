from abc import ABC

from Mobs.Entity import Entity


class SlimeEntity(Entity, ABC):

    def __init__(self):
        self.max_distance = 100
        self.min_distance = 80
        self.offset = 0


class LuminantSlime(SlimeEntity):

    def __init__(self):
        super().__init__()
        self.color = (0, 227, 214)
