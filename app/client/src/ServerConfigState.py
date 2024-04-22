import pygame
from InputBox import InputBox

class ServerConfigState:
    def __init__(self,name,color=(0,0,0)):
        self.name = name
        self.state_machine = None
        self.color = color
        self.font_size_button = 40
        self.font_size_title = 65
        self.ip_address = '127.0.0.1'
        self.port = 3000
        self.text__tp1 = ''
        self.text__tp2 = ''
        self.max_characters = 16
        self.input_box_ip = InputBox(475,202,275,46,self.text__tp1,False)
        self.input_box_port = InputBox(475,257,275,46,self.text__tp2,True)

    def enter(self):
        pass
    
    def leave(self):
        pass
    
    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font_size_button.render(text, True, color)
        surface.blit(text_surface, (x, y))

    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        #Title
        font = pygame.font.SysFont('Georgia',self.font_size_title)
        text = font.render("SERVER CONFIGURATION", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, self.state_machine.window_height//6) 
        window.blit(text, text_rect)

        #IP Address Button
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render("IP Address: ", True, self.color, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2 - 175, 225) 
        window.blit(text, text_rect)

        #Input Box IP Address
        self.input_box_ip.draw(self.state_machine.window)

        #Port Button
        text = font.render("Port: ", True, self.color, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2 - 175, 285) 
        window.blit(text, text_rect)

        #Input Box Port
        self.input_box_port.draw(self.state_machine.window)

        #Current IP/Port Text
        text = font.render((f"Current: '{self.ip_address}:{self.port}'"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 345) 
        window.blit(text, text_rect)

        #Enter Button
        text = font.render("Enter", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2 + 355, 250) 
        window.blit(text, text_rect)

        #ESC Text
        font = pygame.font.SysFont('Georgia',30)
        text = font.render(("Press ESC to go back."), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (150,570)
        window.blit(text, text_rect)

    def update(self):
        for event in pygame.event.get():
            self.input_box_ip.handle_event(event)
            self.input_box_port.handle_event(event)
            current_mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT: #X button is hit
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN: #If a key is hit. Only handles ESC
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("settings")
            elif event.type == pygame.MOUSEBUTTONDOWN: #If the mouse is clicked
                #If mouse is clicked within the text boxes (aka - the buttons)
                print(current_mouse_pos)
                if (current_mouse_pos[0] >= 805 and current_mouse_pos[0] <= 904) and (current_mouse_pos[1] >= 227 and current_mouse_pos[1] <= 274):
                    #When clicked, change the current IP Address and Port to the given values in the input boxes
                    print("Clicked Enter")
                    self.ip_address = self.text__tp1
                    self.port = int(self.text__tp2)