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

        font = pygame.font.SysFont('Georgia',self.font_size_title)
        text = font.render("CHANGE VOLUME", True, self.color, (255,255,255)) 
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

        text = font.render((f"Master Volume: {round(self.state_machine.master_volume * 100,2)}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 400) 
        window.blit(text, text_rect)

    def update(self):
        for event in pygame.event.get():
            current_mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("settings")
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse button clicks
                self.last_input_method = 'mouse'  # Update last input method to mouse on click
                #self.quit_sound.play()
                #time.sleep(0.5)  # Give the sound time to finish
                click_pos = pygame.mouse.get_pos()

                #print(click_pos)

                if (click_pos[0] >= 375 and click_pos[0] <= 625) and (click_pos[1] >= 222 and click_pos[1] <= 278):
                    #print("Volume Up Clicked")
                    if(self.state_machine.master_volume < .9):
                        self.state_machine.master_volume += .1
                elif (current_mouse_pos[0] >= 344 and current_mouse_pos[0] <= 657) and (current_mouse_pos[1] >= 297 and current_mouse_pos[1] <= 353):
                    #print("Volume Down Clicked")
                    if(self.state_machine.master_volume > .1):
                        self.state_machine.master_volume -= .1