import pyglet

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

window = pyglet.window.Window(640, 480)
batch = pyglet.graphics.Batch()

image = pyglet.resource.image('img/scorpio.png')
px = window.width//2 - image.width//2
py = window.height//2 - image.height//2
sprite = pyglet.sprite.Sprite(image, x = px, y = py, batch = batch)

@window.event
def on_draw():
	window.clear()
	batch.draw()

pyglet.app.run()
