import pyglet

window = pyglet.window.Window()
window.push_handlers(pyglet.window.event.WindowEventLogger())

label = pyglet.text.Label('Window events!.', font_name='Monospace', font_size=24, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()
    print("===> Draw <===")

pyglet.app.run()
