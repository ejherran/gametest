import pyglet

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

window = pyglet.window.Window()
image = pyglet.resource.image('img/scorpio.png')

@window.event
def on_draw():
    window.clear()
    image.blit( (window.width//2) - (image.width//2), (window.height//2) - (image.height//2))

pyglet.app.run()
