import pygame
from pygame.math import Vector2
from rectangle import Rectangle
from game import Game
from camera import Camera
from controls import Controls
from car import Car
from line import Line


def main():

    pygame.init()
    Game.init()
    Camera.init()

    position = Vector2(0, 0)
    car = Car(position, 40, 80)

    start = (-500, 1000)
    end = (-500, -1000)

    line = Line(start, end, 4)

    start = (500, 1000)
    end = (500, -1000)

    line2 = Line(start, end, 4)

    while(True):
        
        Controls.update()
        car.move()
        Camera.position = car.position
        Game.display.fill((0, 0, 0))
        line.draw()
        line2.draw()
        car.draw()
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        Game.clock.tick(60)

if __name__ == '__main__':
    main()





