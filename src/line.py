from pickle import FALSE
from turtle import Vec2D
import pygame
from pygame import Vector2
from gamedata import GameData
from camera import Camera

class Line:

    def __init__(self, start: Vector2, end: Vector2, width: float, dotted: bool = False):
        
        self.start = start
        self.end = end
        self.width = width
        self.dotted = dotted

    def update(self):
        pass

    def draw(self):

        start_camera_space_point = Vector2(self.start)
        end_camera_space_point = Vector2(self.end)

        # Move points to camera space
        Camera.to_camera_space(start_camera_space_point)
        Camera.to_camera_space(end_camera_space_point)

        # Move points to screen space
        start_camera_space_point.x = start_camera_space_point.x + GameData.offset.x
        start_camera_space_point.y = -start_camera_space_point.y + GameData.offset.y  
        
        end_camera_space_point.x = end_camera_space_point.x + GameData.offset.x
        end_camera_space_point.y = -end_camera_space_point.y + GameData.offset.y  

        pygame.draw.line(GameData.display, (255, 255, 255), start_camera_space_point, end_camera_space_point, self.width)
