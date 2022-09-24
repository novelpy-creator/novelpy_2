import pygame, sys
from pygame.locals import *
from python import *
pygame.init()
# These dictionary for character, backgrounds, colors, positions and sprites.
image = {}
scene = {}
color = {}
position = {}

# First, we define our character sprites by write image path or defined variables to load_image() function.
image["girl normal"] = graph.load_image("girl_normal.png")
image["girl sad"] = graph.load_image("girl_sad.png")
image["girl upset"] = graph.load_image("girl_upset.png")
image["girl blushed"] = graph.load_image("girl_blushed.png")

# Then, we come to load backgrounds for game state
scene["night meadow"] = graph.load_image("night_meadow.jpg")

# Finally, define some RGB color.
color["black"] = graph.color(0, 0, 0)
color["white"] = graph.color(255, 255, 255)

# Oh! I forgot some positions.
position["left"] = (0, 300)
position["center"] = (400, 300)
position["right"] = (600, 300)

class Girl(manage.Sprite):

    def __init__(self):
        self.image = image["girl normal"]
        self.rect = self.image.get_rect()
        self.rect.center = position["center"]

# Finally, define a scene class.
class StartScene(manage.Scene):
    "The class started scene while you writing your own game."

    def __init__(self):
        super().__init__()
        self.girl = Girl()

    def get_event(self, events):
        for event in events:
            if event.type == QUIT:
                self.girl.kill()
                pygame.quit()
                sys.exit(0)
                
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.next_scene = SecondScene()
                    
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.next_scene = SecondScene()
                
    def update(self):
        self.girl.update()

    def render(self, surface):
        surface.fill(color["white"])
        surface.blit(scene["night meadow"], (0, 0))
        self.girl.draw(surface)
        text.Text([ "???", "Hi! Nice to see you again, player!" ], (20, 440), surface)
        pygame.display.flip()

class SecondScene(manage.Scene):
    "The class started scene while you writing your own game."

    def __init__(self):
        super().__init__()
        self.girl = Girl()

    def get_event(self, events):
        for event in events:
            if event.type == QUIT:
                self.girl.kill()
                pygame.quit()
                sys.exit(0)
                
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    pass
                
    def update(self):
        self.girl.update()

    def render(self, surface):
        surface.fill(color["white"])
        surface.blit(scene["night meadow"], (0, 0))
        self.girl.draw(surface)
        text.Text(["Girl", 'Welcome to PyGame Novel 2.0 version 1.' ], (20, 420), surface)
        pygame.display.flip()
        
class App:

    def __init__(self):
        self.scene = StartScene()
        self.canvas = window.screen.set_display((800, 600))
        window.screen.set_caption("NovelPy Window")
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.scene.render(self.canvas)
            self.scene.get_event(get_event.events())
            self.scene.update()
            self.scene = self.scene.next_scene
            pygame.display.flip()
if __name__ == "__main__":
    app = App()
    app.run()
        
        
