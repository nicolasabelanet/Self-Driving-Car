from typing import Any, List
from gamedata import GameData
from road import Road

class World:

    game_objects: List[Any] = []
    road: Road = None

    @classmethod
    def add(cls, *objects) -> None:
        for object in objects:
            cls.game_objects.append(object)

    @classmethod
    def init(cls) -> None:
        cls.road = Road(0, 90)

    @classmethod
    def update(cls) -> None:
        
        for object in cls.game_objects:
            object.update()
    
    @classmethod
    def draw(cls) -> None:
        GameData.display.fill((190, 190, 190))
        cls.road.draw()        

        for object in cls.game_objects:
            object.draw()