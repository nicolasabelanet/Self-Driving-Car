import pygame
from pygame.math import Vector2
from gamedata import GameData
from camera import Camera
from controls import Controls
from player import Player
from line import Line
from world import World


def main():

    pygame.init()
    GameData.init()
    Camera.init()
    World.init()

    position = Vector2(0, 0)
    car = Player(position, 40, 80)
   
    Camera.follow(car)

    start = (-500, 1000)
    end = (-500, -1000)

    line = Line(start, end, 4)

    start = (500, 1000)
    end = (500, -1000)

    line2 = Line(start, end, 4)

    World.add(line, line2, car)

    while(True):
        
        Camera.update()
        World.update()     
        World.draw()
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        GameData.clock.tick(60)

if __name__ == '__main__':
    main()





