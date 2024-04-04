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

        font = pygame.font.SysFont('Georgia',self.font_size_title)
        text = font.render("SETTINGS", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, self.state_machine.window_height//6) 
        window.blit(text, text_rect)

        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render("Sound", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 250) 
        window.blit(text, text_rect)

        text = font.render("Character", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 325) 
        window.blit(text, text_rect)

        text = font.render("Key Binds", True, self.color, (255,255,255)) 
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
                    self.state_machine.transition("menu")
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse button clicks
                self.last_input_method = 'mouse'  # Update last input method to mouse on click
                #self.quit_sound.play()
                #time.sleep(0.5)  # Give the sound time to finish
                click_pos = pygame.mouse.get_pos()

                #print(click_pos)
                
                # Check if the click is within the bounds of the buttons and act accordingly
                if (click_pos[0] >= 428 and click_pos[0] <= 570) and (click_pos[1] >= 219 and click_pos[1] <= 276):
                    #print("Sound Clicked")
                    self.state_machine.transition("volume")
                elif (current_mouse_pos[0] >= 392 and current_mouse_pos[0] <= 608) and (current_mouse_pos[1] >= 297 and current_mouse_pos[1] <= 353):
                    #print("Char Clicked")
                    self.state_machine.transition("character")
                elif (current_mouse_pos[0] >= 388 and current_mouse_pos[0] <= 612) and (current_mouse_pos[1] >= 371 and current_mouse_pos[1] <= 428):
                    #print("KeyBinds Clicked")
                    self.state_machine.transition("binds")