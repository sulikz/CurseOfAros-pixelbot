from abc import ABC

from Mobs.Entity import Entity


class RaptorEntity(Entity, ABC):

    def __init__(self):
        self.max_distance = 70
        self.min_distance = 50
        self.offset = 0


class Raptor(RaptorEntity):

    def __init__(self):
        super().__init__()
        self.color = [(132, 40, 49)]


class IceRaptor(RaptorEntity):

    def __init__(self):
        super().__init__()
        self.color = [(33, 48, 82)]
