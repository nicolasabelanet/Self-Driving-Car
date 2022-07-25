from cmath import rect
import pyglet
from pyglet import shapes, clock

window = pyglet.window.Window(1440, 1920)
batch = pyglet.graphics.Batch()

circle = shapes.Circle(700, 150, 100, color=(50, 225, 30), batch=batch)
square = shapes.Rectangle(500, 500, 200, 200, color=(55, 55, 255), batch=batch)
rectangle = shapes.Rectangle(720, 960, 400, 200, color=(255, 22, 20), batch=batch)
rectangle.anchor_x = 200
rectangle.anchor_y = 100

rectangle.opacity = 128
rectangle.rotation = 33
line = shapes.Line(100, 100, 100, 200, width=19, batch=batch)
line2 = shapes.Line(150, 150, 444, 111, width=4, color=(200, 20, 20), batch=batch)
star = shapes.Star(800, 400, 60, 40, num_spikes=20, color=(255, 255, 0), batch=batch)

def update(dt):
    rectangle.rotation += 1
    rectangle.position = (720, rectangle.position[1] + 1)
@window.event
def on_draw():
    print("jere")
    window.clear()
    batch.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()