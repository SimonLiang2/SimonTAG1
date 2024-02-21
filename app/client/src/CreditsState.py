import pygame
class CreditsState:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
    
    def enter(self):
        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("menu")