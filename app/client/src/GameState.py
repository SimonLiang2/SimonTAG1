import pygame
class GameState:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        return
    
    def enter(self):
        print(f"Entering: {self.name}")
        return
    
    def leave(self):
        print(f"Leaving: {self.name}")
        return
    
    def render(self,window=None):
        color = (255, 0, 0)
        window.fill(color)
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
        pass