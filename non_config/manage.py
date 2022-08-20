# Scenes state

class Scene(object):

    def __init__(self):
        super().__init__()
        self.next_scene = self

    def get_event(self, events):
        return "I'm sorry but these no events handle state."

    def update(self):
        return "There's no update state."

    def render(self):
        return "No rendering object or anything is added."