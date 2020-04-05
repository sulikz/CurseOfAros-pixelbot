from abc import ABC

from Mobs.Entity import Entity


class FiendEntity(Entity, ABC):

    def __init__(self):
        self.max_distance = 140
        self.min_distance = 80
        self.offset = 50


class ForestFiend(FiendEntity):

    def __init__(self):
        super().__init__()
        self.color = (99, 56, 49)


class IceFiend(FiendEntity):

    def __init__(self):
        super().__init__()
        self.color = (90, 121, 148)


class RockFiend(FiendEntity):

    def __init__(self):
        super().__init__()
        self.color = (66, 40, 57)
