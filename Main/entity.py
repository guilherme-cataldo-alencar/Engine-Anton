import pygame


class Entity:

    def __init__(self, x, y, width, height, sprite_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite_path = sprite_path

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def update(self):
        pass

    def render(self, screen):
        sprite = pygame.image.load(self.sprite_path)
        screen.blit(sprite, (self.get_x(), self.get_y()))