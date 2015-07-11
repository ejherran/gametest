#
#   To play media need install avbin: http://avbin.github.io/AVbin/Home/Home.html
#

import pyglet
from pyglet.window import key

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

music = pyglet.resource.media('sound/tsuna.mp3')                        #   Ambient music (Big file)
sound = pyglet.resource.media('sound/sniper.mp3', streaming=False)      #   Sound effect  (Small file)

window = pyglet.window.Window()
label = pyglet.text.Label('Press ENTER: Play Music. - Press SPACE: Play Sound Effect.', font_name='Monospace', font_size=12, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_key_press(symbol, modifiers):
    
    if symbol == key.ENTER:
        print("Play music!...")        
        music.play()
    
    elif symbol == key.SPACE:
        print("Play sound effect!...")
        sound.play()

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
