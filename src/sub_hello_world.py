import pyglet

class HelloWorldWindow(pyglet.window.Window):
    
    def __init__(self):
        super(HelloWorldWindow, self).__init__()
        self.label = pyglet.text.Label('Hello, world!', font_name='Monospace', font_size=36, x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')

    def on_draw(self):
        self.clear()
        self.label.draw()

if __name__ == '__main__':
    window = HelloWorldWindow()
    pyglet.app.run()
