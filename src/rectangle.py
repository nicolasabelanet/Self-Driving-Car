from camera import Camera
import pygame
from pygame.math import Vector2
from gamedata import GameData
import math 
from typing import Tuple

class Rectangle():

    def __init__(self, position: Vector2, angle: float, width: float, height: float, color: Tuple[int]):
        
        self.__position = position
        self.__angle = angle
        self.width = width
        self.height = height
        self.color = color

        self.radius = math.hypot(self.width, self.height)
        self.alpha = math.atan2(self.width, self.height)

        self.points = tuple(Vector2() for x in range(4))

        self.calculate_points()

    @property
    def position(self) -> Vector2:
        return self.__position

    @position.setter
    def position(self, position) -> None:
        self.__position = position
        self.calculate_points()

    @property
    def angle(self) -> Vector2:
        return self.__angle

    @angle.setter
    def angle(self, angle) -> None:

        self.__angle = angle
        self.calculate_points()


    def calculate_points(self) -> None:
    
        self.points[0].x = self.position.x - math.sin(self.angle - self.alpha) * self.radius
        self.points[0].y = self.position.y - math.cos(self.angle - self.alpha) * self.radius

        self.points[1].x = self.position.x - math.sin(self.angle + self.alpha) * self.radius
        self.points[1].y = self.position.y - math.cos(self.angle + self.alpha) * self.radius

        self.points[2].x = self.position.x - math.sin(math.pi + self.angle - self.alpha) * self.radius
        self.points[2].y = self.position.y - math.cos(math.pi + self.angle - self.alpha) * self.radius

        self.points[3].x = self.position.x - math.sin(math.pi + self.angle + self.alpha) * self.radius
        self.points[3].y = self.position.y - math.cos(math.pi + self.angle + self.alpha) * self.radius

    def draw(self) -> None:

        screen_space_points = tuple(Vector2(point) for point in self.points)

        for point in screen_space_points:

            # Move point to camera space
            Camera.to_camera_space(point)

            # Move point to screen space
            point.x = point.x + GameData.offset.x
            point.y = -point.y + GameData.offset.y  

            #print (point)
    
        pygame.draw.polygon(GameData.display, self.color, screen_space_points)
        