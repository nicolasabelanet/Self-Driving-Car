from car import Car
from pygame.math import Vector2
from controls import Controls


class Player (Car):

    def __init__(self, position: Vector2, width: int, height: int, max_speed: float = 10):
        self.action = [0, 0, 0, 0]
        super().__init__(position, width, height, max_speed)

    def update(self):

        Controls.update()

        self.action = Controls.get_action()

        super().update(self.action)

        