import pyglet
from pyglet.window import key

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

l1x = 0
l1y = 0
l3x = 500
l3y = 300

layer0 = pyglet.graphics.Batch()                                        # Fix background
layer1 = pyglet.graphics.Batch()                                        # Move map
layer2 = pyglet.graphics.Batch()                                        # Player
layer3 = pyglet.graphics.Batch()                                        # Tree

background = pyglet.resource.image('img/desert.png')
bw = background.width
bh = background.height
sbackground = pyglet.sprite.Sprite(background, x = 0, y = 0, batch = layer0)

rmap = pyglet.resource.image('img/obstacle1.png')
smap = pyglet.sprite.Sprite(rmap, x = l1x, y = l1y, batch = layer1)

player = pyglet.resource.image('img/scorpio.png')
px = bw//2 - player.width//2
py = bh//2 - player.height//2
splayer = pyglet.sprite.Sprite(player, x = px, y = py, batch = layer2)

rtree = pyglet.resource.image('img/arbol1.png')
stree = pyglet.sprite.Sprite(rtree, x = l3x, y = l3y, batch = layer3)

window = pyglet.window.Window(bw, bh)

@window.event
def on_text_motion(motion):
    
    global l1y, l1x, l3y, l3x
    
    if motion == key.MOTION_UP:
        l1y -= 2
        l3y -= 2
    elif motion == key.MOTION_DOWN:
        l1y += 2
        l3y += 2
    elif motion == key.MOTION_RIGHT:
        l1x -= 2
        l3x -= 2
    elif motion == key.MOTION_LEFT:
        l1x += 2
        l3x += 2
    
    smap.x = l1x
    smap.y = l1y
    stree.x = l3x
    stree.y = l3y
    
@window.event
def on_draw():
    window.clear()
    layer0.draw()
    layer1.draw()
    layer2.draw()
    layer3.draw()

pyglet.app.run()
