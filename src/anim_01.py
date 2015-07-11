import pyglet

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

layer0 = pyglet.graphics.Batch()
layer1 = pyglet.graphics.Batch()

background = pyglet.resource.image('img/desert.png')
bw = background.width
bh = background.height

tile = pyglet.sprite.Sprite(background, x = 0, y = 0, batch = layer0)

character = pyglet.resource.image('img/scorpio.png')
px = bw//2 - character.width//2
py = 0
sprite = pyglet.sprite.Sprite(character, x = px, y = py, batch = layer1)
sprite.dy = 60

window = pyglet.window.Window(bw, bh)
fps_display = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
    window.clear()
    layer0.draw()
    layer1.draw()
    fps_display.draw()

def update(dt):
    sprite.y += sprite.dy * dt

pyglet.clock.schedule_interval(update, 1/120.0)

pyglet.app.run()
