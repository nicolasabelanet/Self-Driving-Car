from pygame import Vector2
from gamedata import GameData
from typing import Any

class Camera:

    position: Vector2
    target: Any

    @classmethod
    def init(cls):
        cls.position = Vector2(0, 0)

    @classmethod
    def update(cls):
        cls.position.y = cls.target.position.y

    @classmethod
    def to_camera_space(cls, other_position: Vector2) -> Vector2:

        other_position.x -= cls.position.x
        other_position.y -= cls.position.y
        
        # Ensure the drawing coordinates do not get too large
        # while other_position.y > Game.height:
        #     other_position.y -= Game.heights

    @classmethod
    def follow(cls, target):
        cls.target = target