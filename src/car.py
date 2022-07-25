from turtle import pos
import pygame
from pygame.math import Vector2
from controls import Controls
import math
from enum import Enum
from gamedata import GameData
from rectangle import Rectangle
from typing import List

def Direction(Enum):
    FORWARD = 1
    REVERSE = 2
    LEFT = 3
    RIGHT = 4

class Car (Rectangle):

    def __init__(self, position: Vector2, width: int, height: int, max_speed: float = 10):


        self.max_speed = max_speed

        self.speed: float = 0
        self.acceleration: float = 0.2
        self.friction: float = 0.05
        self.destroyed: bool = False

        super().__init__(position, 0, width, height, (255, 255, 255))

    def update(self, action: List[int]):

        forward, reverse, left, right = action

        if forward:
            self.speed += self.acceleration
        
        if reverse:
            self.speed -= self.acceleration
        
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        
        
        if self.speed < (-self.max_speed / 2): 
            self.speed = -self.max_speed / 2
        

        if self.speed > 0 :
            self.speed -= self.friction
        
        if self.speed < 0: 
            self.speed += self.friction
        
        
        if abs(self.speed) < self.friction:
            self.speed = 0

        if self.speed != 0:

            flip = 1 if self.speed > 0 else -1

            if left:
                self.angle -= 0.03 * flip
            

            if right:
                self.angle += 0.03 * flip


        new_position = Vector2()
        new_position.x = math.sin(self.angle) * self.speed
        new_position.y = math.cos(self.angle) * self.speed

        self.position += new_position

    def draw(self):
        super().draw()

    