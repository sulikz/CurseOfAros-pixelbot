from abc import ABC

from Mobs.Entity import Entity


class CyclopsEntity(Entity, ABC):

    def __init__(self):
        self.max_distance = 140
        self.min_distance = 80
        self.offset = 90


class AncientCyclops(CyclopsEntity, ABC):

    def __init__(self):
        super().__init__()
        self.max_distance = 140
        self.min_distance = 80
        self.offset = 80
        self.color = [(24, 142, 156), (33, 121, 148), (41, 85, 115)]
# (99, 130, 148),a
