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
        self.color = [(99, 56, 49)]


class IceFiend(FiendEntity):

    def __init__(self):
        super().__init__()
        self.color = [(90, 121, 148)]


class RockFiend(FiendEntity):

    def __init__(self):
        super().__init__()
        self.color = [(66, 40, 57)]


class SpectralFiend(FiendEntity):

    def __init__(self):
        super().__init__()
        self.min_distance = 90
        self.color = [(156, 52, 189), (156, 113, 189)]


class PhantomFiend(FiendEntity):

    def __init__(self):
        super().__init__()
        self.min_distance = 90
        self.color = [(49, 158, 181), (49, 158, 173), (99, 174, 173)]
