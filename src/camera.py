from turtle import pos, position
from pygame import Vector2
from game import Game

class Camera:

    position: Vector2

    @staticmethod
    def init():
        Camera.position = Vector2(0, 0)

    @staticmethod
    def to_camera_space(other_position: Vector2) -> Vector2:

        other_position.x -= Camera.position.x
        other_position.y -= Camera.position.y
        
        # Ensure the drawing coordinates do not get too large
        # while other_position.y > Game.height:
        #     other_position.y -= Game.height