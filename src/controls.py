import pygame

class Controls:

    up: bool = False
    left: bool = False
    right: bool = False
    down: bool = False

    @staticmethod
    def update():
          
        keys = pygame.key.get_pressed()
                
        if keys[pygame.K_UP]:
            Controls.up = True
        else:
            Controls.up = False

        if keys[pygame.K_LEFT]:
            Controls.left = True
        else:
            Controls.left = False

        if keys[pygame.K_RIGHT]:
            Controls.right = True
        else:
            Controls.right = False

        if keys[pygame.K_DOWN]:
            Controls.down = True
        else:
            Controls.down = False
