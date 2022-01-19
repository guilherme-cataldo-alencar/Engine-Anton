import pygame
from entity import Entity
from player import Player


class Game:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        pygame.display.set_caption(title)
        self.display = pygame.Surface((150,100))
        self.loop = True

        # Inicializando objetos
        self.entities = []

        self.player = Player(10, 10, 16, 16, "Main/player.png")
        self.entities.append(self.player)

    def scaling(self):
        surf = pygame.transform.scale(self.display,(600,400))
        self.window.blit(surf, (0,0))

    def draw(self):
        self.scaling()
        self.display.fill((0, 0, 0))

        # Desenhando as Entidades
        for entitie in self.entities:
            entitie.render(self.display)

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()

            # Update da Entidades
            for entitie in self.entities:
                entitie.update()


game = Game(600, 400, "Game")
game.update()

