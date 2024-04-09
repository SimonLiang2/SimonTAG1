import pygame

class VolumeState:
    def __init__(self,name,color=(0,0,0)):
        self.name = name
        self.state_machine = None
        self.color = color
        self.font_size_button = 50
        self.font_size_title = 80
    
    def enter(self):
        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")

    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        #Title
        font = pygame.font.SysFont('Georgia',self.font_size_title)
        text = font.render("CHANGE VOLUME", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, self.state_machine.window_height//6) 
        window.blit(text, text_rect)

        #Volume Up Button
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render("Volume Up", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 250) 
        window.blit(text, text_rect)

        #Volume Down Button
        text = font.render("Volume Down", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 325) 
        window.blit(text, text_rect)

        #Current Master Volume % Text
        text = font.render((f"Master Volume: {round(self.state_machine.master_volume * 100,2)}%"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 400) 
        window.blit(text, text_rect)

        #ESC Text
        font = pygame.font.SysFont('Georgia',30)
        text = font.render(("Press ESC to go back."), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (150,570)
        window.blit(text, text_rect)

    def update(self):
        for event in pygame.event.get():
            current_mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT: #X button is hit
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN: #If a key is hit. Only handles ESC
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("settings")
            elif event.type == pygame.MOUSEBUTTONDOWN: #If the mouse is clicked
                #If mouse is clicked within the text boxes (aka - the buttons)
                if (current_mouse_pos[0] >= 375 and current_mouse_pos[0] <= 625) and (current_mouse_pos[1] >= 222 and current_mouse_pos[1] <= 278):
                    #When clicked, add .1 to the master volume (max is 1.0)
                    if(self.state_machine.master_volume < .9): #Error checking bounds
                        self.state_machine.master_volume += .1
                elif (current_mouse_pos[0] >= 344 and current_mouse_pos[0] <= 657) and (current_mouse_pos[1] >= 297 and current_mouse_pos[1] <= 353):
                    #When clicked, subtract .1 to the master volume (min is 0.0)
                    if(self.state_machine.master_volume > .1): #Error checking bounds
                        self.state_machine.master_volume -= .1