import pyglet
from pyglet.window import key

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
py = bh//2 - character.height//2
sprite = pyglet.sprite.Sprite(character, x = px, y = py, batch = layer1)


window = pyglet.window.Window(bw, bh)

@window.event
def on_text_motion(motion):
    
    if motion == key.MOTION_UP:
        sprite.y += 2
    elif motion == key.MOTION_DOWN:
        sprite.y -= 2
    elif motion == key.MOTION_RIGHT:
        sprite.x += 2
    elif motion == key.MOTION_LEFT:
        sprite.x -= 2
    
    print(sprite.x, sprite.y)

@window.event
def on_draw():
    window.clear()
    layer0.draw()
    layer1.draw()

pyglet.app.run()
