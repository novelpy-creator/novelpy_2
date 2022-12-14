import pygame, sys
from pygame.locals import *
from python import *
pygame.init()
# Let's load all the important stuff by reading string in the config.py, then parse it with exec.
exec(open("config.py").read())
class Girl(manage.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = image["girl normal"]
        self.rect = self.image.get_rect()
        self.rect.center = position["center"]

# Finally, define a scene class.
class StartScene(manage.Scene):
    "The class started scene while you writing your own game."

    def __init__(self):
        super().__init__()
        self.girl = Girl()
        self.girl.image = image["girl normal"]

    def get_event(self, events):
        for event in events:
            if event.type == QUIT:
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
        self.girl.image = image["girl normal"]

    def get_event(self, events):
        for event in events:
            if event.type == QUIT:
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
        text.Text(["Girl", 'Welcome to PyGame Novel 2.0.0.alpha.' ], (20, 440), surface)
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
            self.dt = int(self.clock.tick(60))
            self.scene.get_event(get_event.events())
            self.scene.render(self.canvas)
            self.scene.update()
            self.scene = self.scene.next_scene
            pygame.display.flip()
if __name__ == "__main__":
    app = App()
    app.run()
        
        
