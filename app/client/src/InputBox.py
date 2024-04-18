import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (75,75,75)

class InputBox:
    def __init__(self, x, y, width, height, text = '', is_port = False):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = GRAY
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.active = False
        self.is_port = is_port

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_mouse_pos = pygame.mouse.get_pos()
            # If the user clicked on the input box, toggle active
            if (current_mouse_pos[0] >= self.x and current_mouse_pos[0] <= (self.x+self.width)) and (current_mouse_pos[1] >= self.y and current_mouse_pos[1] <= (self.y+self.height)):
                self.active = not self.active
            else:
                self.active = False
            # Change the color of the input box when clicked
            self.color = WHITE if self.active else GRAY
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if(len(self.text) <= 15 and self.is_port == False):
                        self.text += event.unicode

                    if(len(self.text) <= 4 and self.is_port == False):
                        self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))