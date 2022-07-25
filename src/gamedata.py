import pygame
from pygame import Vector2

# Game Settings
class GameData:

    width: int
    height: int

    offset: Vector2

    font: pygame.font.Font
    display: pygame.Surface
    clock: pygame.time.Clock

    @classmethod
    def init(cls):
        cls.width = 1440
        cls.height = 1920

        cls.offset = Vector2(cls.width / 2, cls.height / 2)

        cls.font = pygame.font.Font('arial.ttf', 50)
        cls.display = pygame.display.set_mode((cls.width, cls.height))
        GameData.clock = pygame.time.Clock()