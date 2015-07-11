import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()
label = pyglet.text.Label('Use the keyboard and mouse!.', font_name='Monospace', font_size=12, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_key_press(symbol, modifiers):
    print("Key: ", symbol, "Modifiers: ", modifiers)
    
    if symbol == key.ENTER:
        print("Jump!...")

@window.event
def on_mouse_press(x, y, button, modifiers):
    print("X: ", x, "Y: ", y, "Button: ", button, "Modifiers: ", modifiers)
    
    if button == mouse.RIGHT:
        print("Launch rocket!...")

@window.event
def on_draw():
    window.clear()
    label.draw()
    print("===> Draw <===")

pyglet.app.run()
