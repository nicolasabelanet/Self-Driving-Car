from string import hexdigits
import pygame
from pygame import Vector2

# Game Settings
class Game:

    width: int
    height: int

    offset: Vector2

    font: pygame.font.Font
    display: pygame.Surface
    clock: pygame.time.Clock

    @staticmethod
    def init():
        Game.width = 1440
        Game.height = 1920

        Game.offset = Vector2(Game.width / 2, Game.height / 2)

        Game.font = pygame.font.Font('arial.ttf', 50)
        Game.display = pygame.display.set_mode((Game.width, Game.height))
        Game.clock = pygame.time.Clock()