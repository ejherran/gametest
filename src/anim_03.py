import pyglet
from pyglet.window import key

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

bw = 650
bh = 450
steep = 25

layer0 = pyglet.graphics.Batch()                                        # Dinamic background
layer1 = pyglet.graphics.Batch()                                        # Player
layer2 = pyglet.graphics.Batch()                                        # Dinamic foreground

background = pyglet.resource.image('img/desert1.png')
sbackground = pyglet.sprite.Sprite(background, x = 0, y = 0, batch = layer0, group = pyglet.graphics.OrderedGroup(0))
sbackground2 = pyglet.sprite.Sprite(background, x = 2000, y = 0, batch = layer0, group = pyglet.graphics.OrderedGroup(0))

backobj = pyglet.resource.image('img/sec1_bac.png')
sbackobj = pyglet.sprite.Sprite(backobj, x = 650, y = 0, batch = layer0, group = pyglet.graphics.OrderedGroup(1))

player = pyglet.resource.image('img/player.png')
player_seq = pyglet.image.ImageGrid(player, 1, 4)
player_tex_seq = pyglet.image.TextureGrid(player_seq)
sprite = pyglet.sprite.Sprite(player_tex_seq[0], x = 319, y = 95, batch = layer1)
sprite.cur = 0

foreobj = pyglet.resource.image('img/sec1_fore.png')
sforeobj = pyglet.sprite.Sprite(foreobj, x = 650, y = 0, batch = layer2)

def walk(dt):
    
    sprite.cur += 1
    if sprite.cur == 4:
        sprite.cur = 0
    
    sprite.image = player_tex_seq[sprite.cur]

def move(dt):
    
    global steep
        
    sbackground.x -= steep * dt;
    sbackground2.x -= steep * dt;
    sbackobj.x -= steep * dt;
    sforeobj.x -= steep * dt;

    if sbackground.x <= -2000:
        sbackground.x = sbackground2.x + 2000
    
    if sbackground2.x <= -2000:
        sbackground2.x = sbackground.x + 2000

pyglet.clock.schedule_interval(walk, 1/6.0)    
pyglet.clock.schedule_interval(move, 1/120.0)

window = pyglet.window.Window(bw, bh)
fps_display = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
    window.clear()
    layer0.draw()
    layer1.draw()
    layer2.draw()
    fps_display.draw()

pyglet.app.run()
