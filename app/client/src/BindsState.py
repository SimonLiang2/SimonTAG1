import pygame
import sys

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

    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        #Title
        font = pygame.font.SysFont('Georgia',self.font_size_title)
        text = font.render("CUSTOMIZE KEY BINDS", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, self.state_machine.window_height//6) 
        window.blit(text, text_rect)

        #Up Button Text
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render((f"Up Bind: {self.state_machine.keys[0]}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 250) 
        window.blit(text, text_rect)

        #Down Button Text
        text = font.render((f"Down Bind: {self.state_machine.keys[2]}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 325) 
        window.blit(text, text_rect)

        #Left Button Text
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render((f"Left Bind: {self.state_machine.keys[1]}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 400) 
        window.blit(text, text_rect)

        #Right Button Text
        text = font.render((f"Right Bind: {self.state_machine.keys[3]}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 475) 
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
                click_pos = pygame.mouse.get_pos()

                print(click_pos)
                if (current_mouse_pos[0] >= 395 and current_mouse_pos[0] <= 605) and (current_mouse_pos[1] >= 226 and current_mouse_pos[1] <= 272):
                    print("Up Bind Clicked")
                    event = pygame.event.wait()
                    is_valid = False
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False
                        for i in self.state_machine.keys:
                            if(i.lower() != pygame.key.name(event.key)): 
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True):
                        print((f"A new valid key bind is: {pygame.key.name(event.key)}"))
                        self.state_machine.keys[0] = pygame.key.name(event.key).upper()
                elif (current_mouse_pos[0] >= 376 and current_mouse_pos[0] <= 623) and (current_mouse_pos[1] >= 304 and current_mouse_pos[1] <= 347):
                    print("Down Bind Clicked")
                    event = pygame.event.wait()
                    is_valid = False
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False
                        for i in self.state_machine.keys:
                            if(i.lower() != pygame.key.name(event.key)): 
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True):
                        print((f"A new valid key bind is: {pygame.key.name(event.key)}"))
                        self.state_machine.keys[2] = pygame.key.name(event.key).upper()
                elif (current_mouse_pos[0] >= 391 and current_mouse_pos[0] <= 607) and (current_mouse_pos[1] >= 378 and current_mouse_pos[1] <= 423):
                    print("Left Bind Clicked")
                    event = pygame.event.wait()
                    is_valid = False
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False
                        for i in self.state_machine.keys:
                            if(i.lower() != pygame.key.name(event.key)): 
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True):
                        print((f"A new valid key bind is: {pygame.key.name(event.key)}"))
                        self.state_machine.keys[1] = pygame.key.name(event.key).upper()
                elif (current_mouse_pos[0] >= 379 and current_mouse_pos[0] <= 624) and (current_mouse_pos[1] >= 455 and current_mouse_pos[1] <= 498):
                    print("Right Bind Clicked")
                    event = pygame.event.wait()
                    is_valid = False
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False
                        for i in self.state_machine.keys:
                            if(i.lower() != pygame.key.name(event.key)): 
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True):
                        print((f"A new valid key bind is: {pygame.key.name(event.key)}"))
                        self.state_machine.keys[3] = pygame.key.name(event.key).upper()
                    