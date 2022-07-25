import pygame
from rectangle import Rectangle
from pygame import Vector2
from gamedata import GameData

class Road():

    def __init__(self, x: float, width: int, lane_count: int = 3) -> None:
        self.x = x
        self.width = width
        self.lane_count = lane_count

        position = Vector2(0, 0)

        self.background = Rectangle(position, 0, 100, 100, (80, 80, 80))


    def draw(self):
        self.background.draw()