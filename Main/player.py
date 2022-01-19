import pygame
from entity import Entity


class Player(Entity):

    def __init__(self, x, y, width, height, sprite):
        super().__init__(x, y, width, height, sprite)