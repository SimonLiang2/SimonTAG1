import pygame
from MenuButton import MenuButton

class MainMenu:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.active_button_idx = 0
        self.buttons = []
    
    def enter(self):
        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    def play_pressed(self):
        print("PLAY GAME")
    
    def credits_pressed(self):
        print("CREDITS")
    
    def quit_pressed(self):
        print("QUIT GAME")


    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)


        window.blit(self.create_logo("TAG"), (200,50))
        
        play_button = MenuButton("Play", "", self.play_pressed)
        credits_button = MenuButton("Credits", "", self.credits_pressed)
        quit_button = MenuButton("Quit", "", self.quit_pressed)
        self.buttons = [play_button, credits_button, quit_button]

        y = 200
        for i,button in enumerate(self.buttons):
            if i == self.active_button_idx:
                window.blit(button.create_button(active=True), (200,y))
            else: 
                window.blit(button.create_button(), (200,y))
            y+=50

    def create_logo(self, text):
        font = pygame.font.SysFont("Arial", 32)

        logo = font.render(text, True, (255, 0, 0))
        return logo

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN:

                key = event.key

                if key == pygame.K_UP:
                    if self.active_button_idx > 0:
                        self.active_button_idx -= 1
                    else:
                        self.active_button_idx = len(self.buttons) -1
                elif key == pygame.K_DOWN:
                    if len(self.buttons) - 1 > self.active_button_idx:
                        self.active_button_idx += 1
                    else:
                        self.active_button_idx = 0
                elif key == pygame.K_RETURN:
                    self.buttons[self.active_button_idx].pressed()