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
        text = font.render((f"Up Bind: {pygame.key.name(self.state_machine.keys[0]).upper()}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 200)
        window.blit(text, text_rect)

        #Down Button Text
        text = font.render((f"Down Bind: {pygame.key.name(self.state_machine.keys[2]).upper()}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 275)
        window.blit(text, text_rect)

        #Left Button Text
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render((f"Left Bind: {pygame.key.name(self.state_machine.keys[1]).upper()}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 350)
        window.blit(text, text_rect)

        #Right Button Text
        text = font.render((f"Right Bind: {pygame.key.name(self.state_machine.keys[3]).upper()}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 425)
        window.blit(text, text_rect)

        #How To Use Text
        font = pygame.font.SysFont('Georgia',30)
        text = font.render(("Press and hold on a bind button, then enter desired change."), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 500)
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
                #Only handles when the mouse button is held and a key is pressed
                if (current_mouse_pos[0] >= 395 and current_mouse_pos[0] <= 605) and (current_mouse_pos[1] >= 177 and current_mouse_pos[1] <= 223):
                    #When clicked, bind the inputted key for the "up" key
                    event = pygame.event.wait() #Wait for input
                    is_valid = False #assume input key is invalid
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False #assume input key is invalid
                        for i in self.state_machine.keys: #For all currently stored key binds
                            if(i != pygame.key.name(event.key)): #Error checking is input key is already binded
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True): #If key is valid, store it
                        self.state_machine.keys[0] = event.key
                elif (current_mouse_pos[0] >= 377 and current_mouse_pos[0] <= 622) and (current_mouse_pos[1] >= 253 and current_mouse_pos[1] <= 297):
                    #When clicked, bind the inputted key for the "down" key
                    event = pygame.event.wait() #Wait for input
                    is_valid = False #assume input key is invalid
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False #assume input key is invalid
                        for i in self.state_machine.keys: #For all currently stored key binds
                            if(i != pygame.key.name(event.key)): #Error checking is input key is already binded
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True): #If key is valid, store it
                        self.state_machine.keys[2] = event.key
                elif (current_mouse_pos[0] >= 392 and current_mouse_pos[0] <= 609) and (current_mouse_pos[1] >= 328 and current_mouse_pos[1] <= 373):
                    #When clicked, bind the inputted key for the "left" key
                    event = pygame.event.wait() #Wait for input
                    is_valid = False #assume input key is invalid
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False #assume input key is invalid
                        for i in self.state_machine.keys: #For all currently stored key binds
                            if(i != pygame.key.name(event.key)): #Error checking is input key is already binded
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True): #If key is valid, store it
                        self.state_machine.keys[1] = event.key
                elif (current_mouse_pos[0] >= 379 and current_mouse_pos[0] <= 623) and (current_mouse_pos[1] >= 402 and current_mouse_pos[1] <= 448):
                    #When clicked, bind the inputted key for the "right" key
                    event = pygame.event.wait() #Wait for input
                    is_valid = False #assume input key is invalid
                    if(event.type == pygame.KEYDOWN):
                        is_valid = False #assume input key is invalid
                        for i in self.state_machine.keys: #For all currently stored key binds
                            if(i != pygame.key.name(event.key)): #Error checking is input key is already binded
                                is_valid = True
                            else:
                                is_valid = False
                                break
                        
                    if(is_valid == True): #If key is valid, store it
                        self.state_machine.keys[3] = event.key
                    