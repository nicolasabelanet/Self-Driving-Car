import pygame
from typing import List

class Controls:

    up: bool = False
    left: bool = False
    right: bool = False
    down: bool = False

    @classmethod
    def update(cls):
          
        keys = pygame.key.get_pressed()
                
        if keys[pygame.K_UP]:
            cls.up = True
        else:
            cls.up = False

        if keys[pygame.K_LEFT]:
            cls.left = True
        else:
            cls.left = False

        if keys[pygame.K_RIGHT]:
            cls.right = True
        else:
            cls.right = False

        if keys[pygame.K_DOWN]:
            cls.down = True
        else:
            cls.down = False

    @classmethod
    def get_action(cls) -> List[int]:
        return [int(cls.up), int(cls.down), int(cls.left), int(cls.right)] 