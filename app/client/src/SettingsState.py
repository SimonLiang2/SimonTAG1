import pygame

class SettingsState:
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
        text = font.render("SETTINGS", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, self.state_machine.window_height//6) 
        window.blit(text, text_rect)

        #Sound Button
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render("Sound", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 250) 
        window.blit(text, text_rect)

        #Historical Stats Button
        text = font.render("Historical Stats", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 325) 
        window.blit(text, text_rect)

        #Key Binds Button
        text = font.render("Key Binds", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 400) 
        window.blit(text, text_rect)

        #Server Configuration Button
        text = font.render("Server Config", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 475) 
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
                    self.state_machine.transition("menu")
            elif event.type == pygame.MOUSEBUTTONDOWN: #If the mouse is clicked
                #If mouse is clicked within the text boxes (aka - the buttons)
                if (current_mouse_pos[0] >= 428 and current_mouse_pos[0] <= 570) and (current_mouse_pos[1] >= 219 and current_mouse_pos[1] <= 276):
                    #When clicked, transition
                    self.state_machine.transition("volume")
                elif (current_mouse_pos[0] >= 330 and current_mouse_pos[0] <= 669) and (current_mouse_pos[1] >= 297 and current_mouse_pos[1] <= 354):
                    #When clicked, transition
                    self.state_machine.transition("historical")
                elif (current_mouse_pos[0] >= 388 and current_mouse_pos[0] <= 612) and (current_mouse_pos[1] >= 371 and current_mouse_pos[1] <= 428):
                    #When clicked, transition
                    self.state_machine.transition("binds")
                elif (current_mouse_pos[0] >= 352 and current_mouse_pos[0] <= 648) and (current_mouse_pos[1] >= 447 and current_mouse_pos[1] <= 503):
                    #When clicked, transition
                    self.state_machine.transition("configuration")