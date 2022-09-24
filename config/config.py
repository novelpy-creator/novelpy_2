# To use this file, use exec(open('config.py').read()) in your game.py to initalizing your game.

# Loading the image.
image = {
    'girl normal': graph.load_image("girl_normal.png"),
    'girl sad': graph.load_image("girl_normal.png"),
    'girl upset': graph.load_image("girl_normal.png"),
    'girl blushed': graph.load_image("girl_normal.png")
    }

# Don't ignore this!
scene = {
    'night meadow': graph.load_image("night_meadow.jpg")
    }

# This different with the RGB values in in-game init (because this is generated values of them.)
color = {
    'black': (0, 0, 0, 255),
    'white': (255, 255, 255, 255)
    }
# Position. (I'm not sure if I type the position right...)
position = {
    'left': (0, 300),
    'center': (400, 300),
    'right': (600, 300)
    }