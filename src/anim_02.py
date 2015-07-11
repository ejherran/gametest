import pyglet

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

player = pyglet.resource.image('img/player.png')
player_seq = pyglet.image.ImageGrid(player, 1, 4)
player_tex_seq = pyglet.image.TextureGrid(player_seq)
sprite = pyglet.sprite.Sprite(player_tex_seq[0], x = 94, y = 93)
sprite.cur = 0

window = pyglet.window.Window(200, 200)
window.set_location(500, 350)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

def update(dt):
    sprite.cur += 1
    if sprite.cur == 4:
        sprite.cur = 0
    sprite.image = player_tex_seq[sprite.cur]
    print(sprite.cur)

pyglet.clock.schedule_interval(update, 1/6.0)

pyglet.app.run()
