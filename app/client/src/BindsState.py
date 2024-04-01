import pygame
import time

class BindsState:
    def __init__(self,name,color=(0,0,0)):
        self.name = name
        self.state_machine = None
        self.color = color
        self.font_size_button = 40
        self.font_size_title = 65
    
    def enter(self):
        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    # User has selected the play button
    def volume_up_pressed(self):
        #time.sleep(0.4)
        print("VOLUME UP PRESSED")

    # User has selected the credits button
    def character_pressed(self):
        #time.sleep(0.4)
        print("VOLUME DOWN PRESSED")

    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        font = pygame.font.SysFont('Georgia',self.font_size_title)
        text = font.render("CUSTOMIZE KEY BINDS", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, self.state_machine.window_height//6) 
        window.blit(text, text_rect)

        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render("Volume Up", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 250) 
        window.blit(text, text_rect)

        text = font.render("Volume Down", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 325) 
        window.blit(text, text_rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("settings")