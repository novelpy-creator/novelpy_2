# PyGame-Novel-Two (NovelPy Two)
Update
===================================================
- [x] Mouse, keyboard
- [x] Make a new sprite style
- [ ] Choice

Preview
===================================================
![preview_img](https://user-images.githubusercontent.com/108453991/190960355-5b9bac79-7d09-40dc-a26b-2982961c65d3.png)

(The image is for testing if I can change the how the game look.)

The demo is also added a sprite class example can find in those link:
```py
class Sprite(object):

    def __init__(self):
        self.images = []
        self.image = None
        self.rect = None

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def kill():
        self.image.set_alpha(0) # Transparent! By that the sprite has been erased from the screen.

```
